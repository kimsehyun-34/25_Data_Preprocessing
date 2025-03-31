# Data_Preprocessing
> 2025년 Data Preprocessing - 데이터 전처리 강의 자료
-----------
주피터 노트북 커널 설정 절차

### 1.conda 환경을 생성
```
conda create --name kim python=3.6
```

### 2. 공간할당
```
conda init
```

### 3. 환경접속
```
conda activate kim
```

### 5. 라이브러리 설치
```
pip install jupyter notebook
pip install ipykernel
```

### 5. Jupyter 커널 생성
```
python -m ipykernel install --user --name=kim --display-name="kim"
```

### 6. Jupyter Notebook 실행
```
jupyter Notebook
```
