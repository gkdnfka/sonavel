import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
KEY_NAME = os.path.join(ROOT_DIR, '서버 접근용 key .pem 파일')

SERVER_IP = '서버 IP'
SERVER_PORT = '서버 포트'

SSH_USERNAME = '서버 로그인 유저 아이디'

DB_USERNAME = 'DB 로그인 유저 이름'
DB_PWD = 'DB 로그인 비밀번호'
DB_NAME = 'sonavel'

DATA_FILEPATH = os.path.join(ROOT_DIR, 'result', 'result_del_name.csv')
CLASS_CODE = {'디스트로이어': 0,
             '워로드': 1,
             '버서커': 2,
             '홀리나이트': 3,
             '배틀마스터': 4,
             '인파이터': 5,
             '기공사': 6,
             '창술사': 7,
             '스트라이커': 8,
             '데빌헌터': 9,
              '블래스터': 10,
              '호크아이': 11,
              '스카우터': 12,
              '건슬링어': 13,
              '바드': 14,
              '서머너': 15,
              '아르카나': 16,
              '소서리스': 17,
              '데모닉': 18,
              '블레이드': 19,
              '리퍼': 20,
              '도화가': 21,
              '기상술사': 22}
