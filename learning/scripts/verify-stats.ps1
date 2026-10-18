# verify-stats.ps1
# ScottPlot 5 statistics ground-truth verifier.
#
# Cross-checks the JSON archives produced by scottplot5-stats.py and
# scottplot5-api.py against two authoritative truth sources:
#   1. Reflection on the compiled ScottPlot.dll  (semantic stats)
#   2. git ls-files                               (file counts)
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File learning/scripts/verify-stats.ps1
#
# Requires: PowerShell 5+ (.NET Framework), git, a built ScottPlot.dll.

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# -- Path resolution ---------------------------------------------------------
$REPO    = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$SLN     = Join-Path $REPO 'src\ScottPlot5'
$CORE    = Join-Path $SLN 'ScottPlot5'
$CTRL    = Join-Path $SLN 'ScottPlot5 Controls'
$ARCHIVE = Join-Path $REPO 'learning\archive'

Write-Host "Repo root: $REPO" -ForegroundColor Cyan
Write-Host ""

# -- Helpers -----------------------------------------------------------------
function Write-Section($title) {
    Write-Host ""
    Write-Host ("=" * 78) -ForegroundColor DarkGray
    Write-Host $title -ForegroundColor Cyan
    Write-Host ("=" * 78) -ForegroundColor DarkGray
}

function Format-Diff($scriptVal, $truthVal) {
    if ($null -eq $scriptVal) { return ("script: <n/a>  truth: $truthVal") }
    $sv = [int]$scriptVal
    $tv = [int]$truthVal
    $diff = $tv - $sv
    if ($diff -eq 0) {
        return ("script: {0,-6} truth: {1,-6} [OK]" -f $sv, $tv)
    } else {
        $sign = if ($diff -gt 0) { "+$diff" } else { "$diff" }
        return ("script: {0,-6} truth: {1,-6} [FAIL] diff: {2}" -f $sv, $tv, $sign)
    }
}

function Check($scriptVal, $truthVal) {
    if ($null -eq $scriptVal) { return $false }
    return ([int]$scriptVal -eq [int]$truthVal)
}

# ============================================================================
# 1. REFLECTION TRUTH  (semantic stats)
# ============================================================================
Write-Section "1. Reflection truth (semantic stats)"

$dllCandidates = @(
    (Join-Path $CORE 'bin\Debug\net462\ScottPlot.dll'),
    (Join-Path $CORE 'bin\Debug\net8.0\ScottPlot.dll'),
    (Join-Path $CORE 'bin\Release\net462\ScottPlot.dll')
)
$dllPath = $null
foreach ($c in $dllCandidates) { if (Test-Path $c) { $dllPath = $c; break } }

if (-not $dllPath) {
    Write-Host "[ERROR] No compiled ScottPlot.dll found. Run: dotnet build" -ForegroundColor Red
    $dllCandidates | ForEach-Object { Write-Host "    $_" }
    exit 1
}
Write-Host "Loading assembly: $dllPath"

# Resolve SkiaSharp / HarfBuzzSharp from the DLL directory
$dllDir = Split-Path $dllPath -Parent
$onResolve = [System.ResolveEventHandler]{
    param($s, $e)
    $name = ($e.Name -split ',')[0]
    $candidate = Join-Path $dllDir "$name.dll"
    if (Test-Path $candidate) { return [System.Reflection.Assembly]::LoadFrom($candidate) }
    return $null
}
[System.AppDomain]::CurrentDomain.add_AssemblyResolve($onResolve)

$asm      = [System.Reflection.Assembly]::LoadFrom($dllPath)
$allTypes = $asm.GetTypes()
$pubTypes = $asm.GetExportedTypes()

$R = @{}   # reflection results

# 1.1 public type count
$R['public_types'] = $pubTypes.Count
Write-Host ("  public types          : {0}" -f $R['public_types'])

# 1.2 public members by kind (DeclaredOnly)
$methods=0; $properties=0; $fields=0; $events=0; $ctors=0; $operators=0; $indexers=0
foreach ($t in $pubTypes) {
    $members = $t.GetMembers([System.Reflection.BindingFlags]'Public,Instance,Static,DeclaredOnly')
    foreach ($m in $members) {
        switch ($m.MemberType) {
            'Method' {
                if ($m.IsSpecialName) {
                    if ($m.Name -like 'op_*') { $operators++ }
                    elseif ($m.Name -like 'get_Item' -or $m.Name -like 'set_Item') { $indexers++ }
                } else { $methods++ }
            }
            'Property'    { $properties++ }
            'Field'       { $fields++ }
            'Event'       { $events++ }
            'Constructor' { $ctors++ }
        }
    }
}
$R['methods']    = $methods
$R['properties'] = $properties
$R['fields']     = $fields
$R['events']     = $events
$R['ctors']      = $ctors
$R['operators']  = $operators
$R['indexers']   = $indexers
$R['members_total'] = $methods + $properties + $fields + $events + $ctors + $operators
Write-Host ("  public members (total): {0}" -f $R['members_total'])
Write-Host ("    method={0} property={1} field={2} ctor={3} operator={4} indexer={5}" `
    -f $methods, $properties, $fields, $ctors, $operators, $indexers)

# 1.3 public interface count (top-level public + nested public)
$pubIfaces = $allTypes | Where-Object { $_.IsInterface -and ($_.IsPublic -or $_.IsNestedPublic) }
$R['public_interfaces'] = @($pubIfaces).Count
Write-Host ("  public interfaces     : {0}" -f $R['public_interfaces'])

# 1.4 interface implementers (public, non-interface)
function Count-Implementers($ifaceName) {
    $iface = $asm.GetType($ifaceName)
    if (-not $iface) { return -1 }
    $impl = $allTypes | Where-Object {
        $_.IsPublic -and -not $_.IsInterface -and
        $iface.IsAssignableFrom($_) -and $_ -ne $iface
    }
    return @($impl).Count
}
$R['icolormap_impl']  = Count-Implementers 'ScottPlot.IColormap'
$R['ipalette_impl']   = Count-Implementers 'ScottPlot.IPalette'
$R['iplottable_impl'] = Count-Implementers 'ScottPlot.IPlottable'
Write-Host ("  IColormap implementers : {0}" -f $R['icolormap_impl'])
Write-Host ("  IPalette  implementers : {0}" -f $R['ipalette_impl'])
Write-Host ("  IPlottable implementers: {0}" -f $R['iplottable_impl'])

# 1.5 PlottableAdder public methods (exclude Get* and special-name)
$adder = $asm.GetType('ScottPlot.PlottableAdder')
if ($adder) {
    $adderMethods = $adder.GetMethods([System.Reflection.BindingFlags]'Public,Instance,Static,DeclaredOnly') |
        Where-Object { -not $_.IsSpecialName -and $_.Name -notlike 'Get*' }
    $R['plot_add_methods'] = @($adderMethods).Count
} else {
    $R['plot_add_methods'] = -1
}
Write-Host ("  PlottableAdder methods : {0} (non-Get*)" -f $R['plot_add_methods'])

# 1.6 enum member counts
function Count-EnumMembers($enumName) {
    $e = $asm.GetType($enumName)
    if (-not $e -or -not $e.IsEnum) { return -1 }
    return @($e.GetEnumNames()).Count
}
$R['MarkerShape'] = Count-EnumMembers 'ScottPlot.MarkerShape'
$R['ArrowShape']  = Count-EnumMembers 'ScottPlot.ArrowShape'
$R['Edge']        = Count-EnumMembers 'ScottPlot.Edge'
$R['Alignment']   = Count-EnumMembers 'ScottPlot.Alignment'
Write-Host ("  enums: MarkerShape={0} ArrowShape={1} Edge={2} Alignment={3}" `
    -f $R['MarkerShape'], $R['ArrowShape'], $R['Edge'], $R['Alignment'])

# ============================================================================
# 2. GIT LS-FILES TRUTH  (file counts)
# ============================================================================
Write-Section "2. git ls-files truth (file counts)"

# Filter helper: match the script's cs_files() exclusion of generated files
function Is-SourceCs($path) {
    return ($path -like '*.cs' -and $path -notlike '*.Designer.cs' -and $path -notlike '*.g.cs')
}

# Core library: per top-level directory (recursive, matches script's cs_files)
$gitCore = @{}
$allCoreFiles = git -C $REPO ls-files "src/ScottPlot5/ScottPlot5/" 2>$null | Where-Object { Is-SourceCs $_ }
foreach ($f in $allCoreFiles) {
    $parts = $f -split '/'
    # src/ScottPlot5/ScottPlot5/<Dir>/...  -> parts[3] is the top-level dir
    if ($parts.Length -ge 5) {
        $dir = $parts[3]
        $gitCore[$dir] = ($gitCore[$dir] + 1)
    } elseif ($parts.Length -eq 4) {
        # src/ScottPlot5/ScottPlot5/<File>.cs -> root scatter file
        $gitCore['(root-scatter)'] = ($gitCore['(root-scatter)'] + 1)
    }
}

Write-Host "  Core library .cs per directory (git tracked, excl. .Designer/.g):"
$gitCore.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host ("    {0,-28} {1,4}" -f $_.Key, $_.Value)
}
$gitCoreTotal = ($gitCore.Values | Measure-Object -Sum).Sum
Write-Host ("  Core total: {0} .cs files" -f $gitCoreTotal)

# Count direct (non-recursive) .cs files under a given repo-relative directory
function Count-DirectCs($relDir) {
    $prefix = "src/ScottPlot5/ScottPlot5/$relDir/"
    $files = git -C $REPO ls-files $prefix 2>$null | Where-Object {
        (Is-SourceCs $_) -and ($_ -replace [regex]::Escape($prefix), '') -notmatch '/'
    }
    return @($files).Count
}

# Key subdirectories
$sub = @{}
$sub['Plottables/Interactive']            = Count-DirectCs 'Plottables/Interactive'
$sub['Rendering/RenderActions']           = Count-DirectCs 'Rendering/RenderActions'
$sub['Interactivity/UserActions']         = Count-DirectCs 'Interactivity/UserActions'
$sub['Interactivity/UserActionResponses'] = Count-DirectCs 'Interactivity/UserActionResponses'
$sub['Plottables root']                   = Count-DirectCs 'Plottables'
$sub['Plottables total (recursive)']      = @($allCoreFiles | Where-Object { $_ -like 'src/ScottPlot5/ScottPlot5/Plottables/*' }).Count

Write-Host ""
Write-Host "  Key subdirectories:"
$sub.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host ("    {0,-38} {1,4}" -f $_.Key, $_.Value)
}

# Platform controls (exclude .Designer.cs to match script's cs_files)
$gitControls = @{}
$ctrlFiles = git -C $REPO ls-files "src/ScottPlot5/ScottPlot5 Controls/" 2>$null | Where-Object { Is-SourceCs $_ }
foreach ($f in $ctrlFiles) {
    $parts = $f -split '/'
    # src/ScottPlot5/ScottPlot5 Controls/<Platform>/...
    if ($parts.Length -ge 5) {
        $plat = $parts[3]
        $gitControls[$plat] = ($gitControls[$plat] + 1)
    }
}
Write-Host ""
Write-Host "  Platform controls .cs per project:"
$gitControls.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host ("    {0,-24} {1,4}" -f $_.Key, $_.Value)
}
$gitControlsTotal = ($gitControls.Values | Measure-Object -Sum).Sum
Write-Host ("  Controls total: {0} .cs files" -f $gitControlsTotal)

# ============================================================================
# 3. DIFF AGAINST ARCHIVE JSON
# ============================================================================
Write-Section "3. Diff against archive JSON"

$statsJson = Get-ChildItem $ARCHIVE -Filter 'scottplot5-stats-v*.json' -ErrorAction SilentlyContinue |
    Sort-Object Name -Descending | Select-Object -First 1
$apiJson = Get-ChildItem $ARCHIVE -Filter 'scottplot5-api-v*.json' -ErrorAction SilentlyContinue |
    Sort-Object Name -Descending | Select-Object -First 1

$hasStats = $null -ne $statsJson
$hasApi   = $null -ne $apiJson

if (-not $hasStats -and -not $hasApi) {
    Write-Host "[INFO] No stats/api JSON archives found in archive/. Skipping diff." -ForegroundColor Yellow
    Write-Host "       Run: python learning/scripts/scottplot5-stats.py --out learning/archive"
    exit 0
}

# -- 3a. stats JSON ---------------------------------------------------------
if ($hasStats) {
    Write-Host ""
    Write-Host ("Comparing stats archive: {0}" -f $statsJson.Name) -ForegroundColor Yellow
    $s = Get-Content $statsJson.FullName -Raw | ConvertFrom-Json

    Write-Host ""
    Write-Host "  [Core library layout - file counts]"
    # JSON stores root-scatter files under a localized key (e.g. "(根目录散文件)");
    # find it dynamically to avoid hardcoding non-ASCII in this script.
    $jsonRootKey = ($s.core_layout.PSObject.Properties.Name | Where-Object { $_ -like '(*' } | Select-Object -First 1)
    foreach ($dir in ($gitCore.Keys | Sort-Object)) {
        $sv = $null
        if ($dir -eq '(root-scatter)') {
            if ($jsonRootKey) { $sv = $s.core_layout.$jsonRootKey }
        } elseif ($s.core_layout.PSObject.Properties.Name -contains $dir) {
            $sv = $s.core_layout.$dir
        }
        $tv = $gitCore[$dir]
        $flag = if (Check $sv $tv) { '[OK]  ' } else { '[FAIL]' }
        Write-Host ("    {0} {1,-26} {2}" -f $flag, $dir, (Format-Diff $sv $tv))
    }

    Write-Host ""
    Write-Host "  [Key subdirectories - file counts]"
    $subMap = @{
        'Plottables/Interactive'            = @{ s = $s.plottables.by_dir.Interactive; t = $sub['Plottables/Interactive'] }
        'Rendering/RenderActions'           = @{ s = $s.render_pipeline.render_action_files; t = $sub['Rendering/RenderActions'] }
        'Interactivity/UserActions'         = @{ s = @($s.interactivity.user_actions).Count; t = $sub['Interactivity/UserActions'] }
        'Interactivity/UserActionResponses' = @{ s = @($s.interactivity.responses).Count; t = $sub['Interactivity/UserActionResponses'] }
        'Plottables root'                   = @{ s = $s.plottables.root; t = $sub['Plottables root'] }
        'Plottables total'                  = @{ s = $s.plottables.total; t = $sub['Plottables total (recursive)'] }
    }
    foreach ($k in ($subMap.Keys | Sort-Object)) {
        $sv = $subMap[$k].s; $tv = $subMap[$k].t
        $flag = if (Check $sv $tv) { '[OK]  ' } else { '[FAIL]' }
        Write-Host ("    {0} {1,-36} {2}" -f $flag, $k, (Format-Diff $sv $tv))
    }

    Write-Host ""
    Write-Host "  [Platform controls - file counts]"
    foreach ($plat in ($gitControls.Keys | Sort-Object)) {
        $sv = $null
        if ($s.platform_controls.PSObject.Properties.Name -contains $plat) { $sv = $s.platform_controls.$plat.files }
        $tv = $gitControls[$plat]
        $flag = if (Check $sv $tv) { '[OK]  ' } else { '[FAIL]' }
        Write-Host ("    {0} {1,-24} {2}" -f $flag, $plat, (Format-Diff $sv $tv))
    }

    Write-Host ""
    Write-Host "  [Semantic stats - reflection truth]"
    $semMap = @(
        @{ n = 'interfaces (public)';   s = $s.interfaces.total;           t = $R['public_interfaces'] }
        @{ n = 'Plot.Add methods';      s = $s.plot_add.method_count;     t = $R['plot_add_methods'] }
        @{ n = 'IColormap impl';        s = @($s.colormaps).Count;        t = $R['icolormap_impl'] }
        @{ n = 'IPalette impl';         s = @($s.palettes).Count;         t = $R['ipalette_impl'] }
        @{ n = 'IPlottable impl';       s = ($s.plottables.by_class_declaration.normal + $s.plottables.by_class_declaration.interactive); t = $R['iplottable_impl'] }
        @{ n = 'render steps';          s = @($s.render_pipeline.steps).Count; t = $sub['Rendering/RenderActions'] }
        @{ n = 'enum MarkerShape';      s = $s.enums.MarkerShape;         t = $R['MarkerShape'] }
        @{ n = 'enum ArrowShape';       s = $s.enums.ArrowShape;          t = $R['ArrowShape'] }
        @{ n = 'enum Edge';             s = $s.enums.Edge;                t = $R['Edge'] }
        @{ n = 'enum Alignment';        s = $s.enums.Alignment;           t = $R['Alignment'] }
    )
    foreach ($item in $semMap) {
        $flag = if (Check $item.s $item.t) { '[OK]  ' } else { '[FAIL]' }
        Write-Host ("    {0} {1,-22} {2}" -f $flag, $item.n, (Format-Diff $item.s $item.t))
    }
}

# -- 3b. api JSON -----------------------------------------------------------
if ($hasApi) {
    Write-Host ""
    Write-Host ("Comparing api archive: {0}" -f $apiJson.Name) -ForegroundColor Yellow
    $a = Get-Content $apiJson.FullName -Raw | ConvertFrom-Json
    $t = $a.totals

    Write-Host ""
    Write-Host "  [Public API surface]"
    $apiMap = @(
        @{ n = 'public types'; s = $t.types; t = $R['public_types'] }
        @{ n = 'members total'; s = $t.members; t = $R['members_total'] }
        @{ n = 'method'; s = $t.by_kind.method; t = $R['methods'] }
        @{ n = 'property'; s = $t.by_kind.property; t = $R['properties'] }
        @{ n = 'field'; s = $t.by_kind.field; t = $R['fields'] }
        @{ n = 'ctor'; s = $t.by_kind.ctor; t = $R['ctors'] }
        @{ n = 'operator'; s = $t.by_kind.operator; t = $R['operators'] }
        @{ n = 'indexer'; s = $t.by_kind.indexer; t = $R['indexers'] }
    )
    foreach ($item in $apiMap) {
        $flag = if (Check $item.s $item.t) { '[OK]  ' } else { '[FAIL]' }
        Write-Host ("    {0} {1,-14} {2}" -f $flag, $item.n, (Format-Diff $item.s $item.t))
    }
    Write-Host ""
    Write-Host "  Note: api.py counts only SOURCE-declared public members." -ForegroundColor DarkGray
    Write-Host "        It omits compiler-generated members (record synthesized" -ForegroundColor DarkGray
    Write-Host "        Equals/GetHashCode/ToString/copy-ctor/==/!= etc.)." -ForegroundColor DarkGray
    Write-Host "        Type count matches reflection; member diffs are expected." -ForegroundColor DarkGray
}

# ============================================================================
# 4. SUMMARY
# ============================================================================
Write-Section "4. Summary"
Write-Host "  Truth sources:" -ForegroundColor Cyan
Write-Host "    Semantic stats -> reflection on compiled ScottPlot.dll (public scope)"
Write-Host "    File counts    -> git ls-files (tracked only, excludes bin/obj)"
Write-Host ""
Write-Host "  Expected matches : file counts, type count, enum members,"
Write-Host "                     public interfaces, IPlottable implementers"
Write-Host "  Expected diffs   : api member count (script omits compiler-generated),"
Write-Host "                     stats Colormap count (script includes internal),"
Write-Host "                     stats Plot.Add count (script regex misses multi-line sigs)"
Write-Host ""
Write-Host "  Any [FAIL] not explained above = check source or script logic." -ForegroundColor Yellow
