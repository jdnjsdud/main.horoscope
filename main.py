import streamlit as st
import random
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 운세", page_icon="🔮")

# 12지신 리스트
zodiac_signs = [
    "쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠",
    "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"
]

# 운세 문구 리스트 (예시)
fortunes = [
    "오늘은 뜻밖의 행운이 찾아오는 날입니다. 기회를 놓치지 마세요!",
    "가까운 사람과의 사소한 오해가 생길 수 있으니 말조심하는 것이 좋습니다.",
    "새로운 도전을 시작하기에 아주 좋은 하루입니다. 자신감을 가지세요.",
    "금전운이 크게 상승하고 있습니다. 뜻밖의 수익이나 선물을 기대해볼 만합니다.",
    "체력이 조금 떨어질 수 있는 날입니다. 무리하지 말고 충분한 휴식을 취하세요.",
    "그동안 묵묵히 노력했던 일들이 드디어 빛을 발하는 하루입니다.",
    "조금은 여유를 가지고 주변을 둘러보세요. 소소하고 확실한 행복이 기다리고 있습니다.",
    "예상치 못한 어려운 일이 생겨도 귀인의 도움을 받아 쉽게 풀릴 것입니다."
]

st.title("🔮 오늘의 띠별 운세")

# 오늘 날짜 출력
today_str = datetime.now().strftime("%Y년 %m월 %d일")
st.write(f"**오늘의 날짜:** {today_str}")
st.divider()

# 띠 선택 드롭다운
selected_zodiac = st.selectbox("자신의 띠를 선택해주세요:", zodiac_signs)

# 운세 보기 버튼
if st.button("운세 보기 🍀"):
    # 띠와 날짜를 조합하여 고유 시드(seed) 생성
    # 이렇게 하면 하루 동안은 같은 띠를 선택했을 때 계속 같은 운세가 나옵니다.
    seed_string = selected_zodiac + datetime.now().strftime("%Y%m%d")
    random.seed(seed_string)

    # 운세 랜덤 선택
    daily_fortune = random.choice(fortunes)

    # 결과 출력
    st.success(f"**{selected_zodiac}**의 오늘 운세입니다!")
    st.info(daily_fortune)