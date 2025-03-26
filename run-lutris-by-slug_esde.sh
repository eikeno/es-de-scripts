#!/usr/bin/env bash
# Wrapper to run Lutris game identified by its slug, from an external application.

lutris "lutris:rungame/${*// /-}"
