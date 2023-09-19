#for prog in wk2a wk2b wk3a wk3b wk4a wk4b wk5a wk5b wk6a wk6b wk7a wk7b wk8a wk8b wk9a wk9b wk10a wk10b wk11b
for prog in compare-senti
do
    python3 ${prog}.py > ${prog}-out.txt
    pygmentize -f html -O full -o ${prog}.html ${prog}.py
done
