import json

# 질문과 답변 저장
data = [
    {
        "role": "system",
        "content": "assistant는 유능한 광고 콘텐츠 제작자이다.",
    },
    {
        "role": "assistant",
        "content":
            "판매란 온라인, 앱, 전화, 매장을 통한 판매를 촉진하는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 제작 목표의 판매란 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "판매란 온라인, 앱, 전화, 매장을 통한 판매를 촉진하는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 제작 목표의 리드란 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "리드란 고객의 액션을 유도하여 리드 및 다른 전환를 늘리는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 제작 목표의 웹사이트 트래픽이란 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "웹사이트 트래픽이란 관련성이 높은 사용자가 웹사이트를 방문하도록 유도합니다.",
    },
    {
        "role": "user",
        "content": "광고의 제작 목표의 앱 프로모션이란 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "앱 프로모션은 앱의 설치 수, 참여도 및 사전 등록을 늘리는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 유형의 검색은 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "검색이란 검색에서 구매 의도가 높은 고객에게 노출하는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 유형의 디스플레이는 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "디스플레이란 눈에 잘 띄는 광고 소재로 사이트와 앱을 통해 고객에게 도달하는 것입니다.",
    },
    {
        "role": "user",
        "content": "광고의 유형의 쇼핑은 무엇인가요? ",
    },
    {
        "role": "assistant",
        "content":
            "쇼핑이란 쇼핑객이 구매할 제품을 살펴볼 때 나의 상품을 표시하는 것입니다.",
    },
    {
        "role": "user",
        "content":
            "광고의 제목 , 설명을 만들어주고, 답변을 Json 형식으로 해줘 설명은 30자이상으로 해주고 메인 키워드와 관련된 추천 키워드 3개와 현재 광고 유형을 알려줘.",
    },
    {
        "role": "user",
        "content":
            "앞으로 대답은 무조건 한국어로 해줘",
    },
    {
        "role": "assistant",
        "content": str({
            "ad_title": "광고 제목",
            "ad_description": "설명",
            "ad_Main_keyword": "메인 키워드",
            "ad_keyword": "추천 키워드1, 추천 키워드2, 추천 키워드3",
            "ad_type": "광고 유형",
            "ad_category": "카테고리",
        }),
    },
    {
        "role": "user",
        "content":
            "무조건 위와 같은 형식으로 답변해줘, 위의 형식을 벗어나면 안돼",
    },
    {
        "role": "user",
        "content":str({
            "광고 목표": "판매",
            "광고 유형": "검색",
            "카테고리": "여행",
            "메인 키워드": "제주도 자전거 여행",
            "연령대": "18세~24세",
            "성별": "여자",
        }),
    },
    {
        "role": "assistant",
        "content": str({
            "ad_title": "여자를 위한 제주도 자전거 여행",
            "ad_description": "아름다운 제주도의 자연을 만끽하며 자전거를 타는 특별한 경험을 느껴보세요. 친구, 가족, 연인과 함께 즐기는 잊지 못할 추억, 제주도의 다양한 문화와 역사를 배울 수 있는 기회입니다.",
            "ad_Main_keyword": "제주도 자전거 여행",
            "ad_keyword": "여행, 자전거 여행, 자전거 렌트",
            "ad_type": "검색",
            "ad_category": "여행",
        }),
    },
    {
        "role": "user",
        "content":str({
            "광고 목표": "판매",
            "광고 유형": "검색",
            "카테고리": "여행",
            "메인 키워드": "제주도 자전거 여행",
            "연령대": "13세 이하",
            "성별": "남자",
        }),
    },
    {
        "role": "assistant",
        "content": str({
            "ad_title": "액션가득! 제주도 킥보드 여행으로 재밌는 여름을 만끽해보세요!",
            "ad_description": "제주도 자전거 여행으로 행복한 순간을 만나보세요! 지금 예약하고 특별 혜택을 놓치지 마세요!",
            "ad_Main_keyword": "제주도 자전거 여행",
            "ad_keyword": "여행, 가족 여행 제주도, 자전거 렌트",
            "ad_type": "검색",
            "ad_category": "여행",
        }),
    },
    {
        "role": "user",
        "content":
            "무조건 위와 같은 형식으로 답변해줘",
    },
    {
        "role": "user",
        "content": "ad_type은 디스플레이, 검색 , 동영상 이 세개로만 대답해줘",
    },
];