#!/bin/bash
{comment_line_1}git clone --depth 1 {source_git} /var/www/{site}/html
{comment_line_2}git clone --depth 1 {database_git} /var/www/{site}/db