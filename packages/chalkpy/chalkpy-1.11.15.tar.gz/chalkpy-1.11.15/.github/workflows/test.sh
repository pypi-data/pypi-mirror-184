#!/usr/bin/env bash
set -exuo pipefail

CHALKPY_VERSION="1.11.15"

if [[ "$CHALKPY_VERSION" =~ ^[0-9]+(\.[0-9]+)*$ ]]; then
  echo "Version is valid"
else
  echo "Invalid version string"
  exit 1
fi
