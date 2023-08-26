#!/bin/bash

echo "[$$] Runinig"
exit $(($$ % 2))
