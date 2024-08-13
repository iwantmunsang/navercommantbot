from cx_Freeze import setup, Executable

# 설치 정보 설정
setup(
    name="navercomandbot",
    version="0.1",
    description="My Python Application",
    executables=[
        Executable("app.py"),
        Executable("main.py")
        ],
)
