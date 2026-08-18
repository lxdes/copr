#!/usr/bin/env bash
#
# check_versions.sh - Check spec file versions against GitHub latest releases
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Default to the parent directory (where copr repos live)
COPR_DIR="${1:-$SCRIPT_DIR}"

echo "=========================================="
echo "  Spec File Versions vs GitHub Latest"
echo "=========================================="
echo ""

for spec in "$COPR_DIR"/**/*.spec; do
    [ -f "$spec" ] || continue

    # Extract crate macro if defined
    crate=""
    crate_line=$(grep -m1 '^%global crate ' "$spec" 2>/dev/null || echo "")
    if [ -n "$crate_line" ]; then
        crate=$(echo "$crate_line" | awk '{print $3}')
    fi

    # Resolve Name
    name_line=$(grep -m1 '^Name:' "$spec" | head -1)
    name_raw=$(echo "$name_line" | awk '{print $2}')

    # Resolve %{crate} and %{name} macros in name
    if [[ "$name_raw" == "%{crate}" ]] && [ -n "$crate" ]; then
        name="$crate"
    elif [[ "$name_raw" == "%{name}" ]]; then
        name="$crate"
    else
        name="$name_raw"
    fi

    # Extract version (resolve simple macros)
    version_line=$(grep -m1 '^Version:' "$spec" | head -1)
    version_raw=$(echo "$version_line" | awk '{$1=""; print $2}' | sed 's/^[[:space:]]*//')

    # Resolve URL - expand macros
    url_line=$(grep -m1 '^URL:' "$spec" | head -1)
    url_raw=$(echo "$url_line" | awk '{print $2}')

    # Replace %{name} with resolved name, %{crate} with crate
    url=$(echo "$url_raw" | sed "s/%{name}/$name/g; s/%{crate}/$crate/g")

    # Extract GitHub owner and repo from URL
    if [[ "$url" =~ github\.com/([^/]+)/([^/.]+) ]]; then
        owner="${BASH_REMATCH[1]}"
        repo="${BASH_REMATCH[2]}"
    else
        echo "  Package: $name"
        echo "  Spec version:  $version_raw"
        echo "  GitHub:        (no valid GitHub URL found)"
        echo ""
        continue
    fi

    # Fetch latest release from GitHub API
    latest_json=$(curl -sf "https://api.github.com/repos/$owner/$repo/releases/latest" 2>/dev/null || echo "")

    if [ -z "$latest_json" ]; then
        echo "  Package: $name"
        echo "  Spec version:  $version_raw"
        echo "  GitHub:        (no releases found or API error)"
        echo ""
        continue
    fi

    latest_tag=$(echo "$latest_json" | jq -r '.tag_name // empty')
    [ -n "$latest_tag" ] || latest_tag="(no tag)"

    # Clean version: strip 'v' prefix if present
    github_version=$(echo "$latest_tag" | sed 's/^v//' )

    echo "  Package: $name"
    echo "  Spec version:  $version_raw"
    echo "  GitHub latest: $github_version (tag: $latest_tag)"
    echo ""
done

echo "=========================================="
echo "  Done"
echo "=========================================="
