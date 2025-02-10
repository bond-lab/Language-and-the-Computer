if [ -d "./venv" ]
then
    source ./venv/bin/activate
    pip install -r requirements.txt
else
    python3.9 -m venv "./venv"
    source ./venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
fi


#for prog in wk2a wk2b wk3a wk3b wk4a wk4b wk5a wk5b wk6a wk6b wk7a wk7b wk8a wk8b wk9a wk9b wk10a wk10b wk11b
for prog in   wk02b wk02c
do
    pygmentize -f html -O full -o ${prog}.html ${prog}.py
    python3 ${prog}.py > ${prog}-out.txt
    #pygmentize -f html -O full -o test_${prog}.html test_${prog}.py
    #pytest -v  test_${prog}.py > test_${prog}-out.txt
done
