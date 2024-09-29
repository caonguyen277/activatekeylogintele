@echo off
REM Thêm tất cả các thay đổi vào Git
git add .

REM Thực hiện commit với thông điệp mặc định
git commit -m "commit"

REM Đẩy thay đổi lên remote repository
git push

pause
