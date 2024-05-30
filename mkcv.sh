#! /bin/sh

mkdir cv-dir
lualatex \
    --jobname Piras_Luca_CV \
    --output-directory=cv-dir \
    Piras_Luca_CV.tex
mv cv-dir/Piras_Luca_CV.pdf static
rm -r cv-dir
