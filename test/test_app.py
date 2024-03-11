import streamlit as st
from streamlit_elements import elements, mui, html
import streamlit as st

# 페이지 설정을 통해 레이아웃을 wide로 설정합니다.
st.set_page_config(layout="wide")

with elements("multiple_children"):

    # <Button> 요소 안에 여러 자식 요소를 추가하는 예시
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   Hello world
    # </Button>

    mui.Button(
        mui.icon.EmojiPeople, mui.icon.DoubleArrow, "Button with multiple children"
    )

    # <Button> 요소 안에 <EmojiPeople />, <DoubleArrow />, <Typography>를
    # 자식으로 추가하는 예시
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   <Typography>
    #     Hello world
    #   </Typography>
    # </Button>

    with mui.Button:
        mui.icon.EmojiPeople()
        mui.icon.DoubleArrow()
        mui.Typography("Button with multiple children")


########
with elements("nested_children"):

    # <Paper> 요소 안에 중첩된 자식 요소를 추가하는 예시
    #
    # <Paper>
    #   <Typography>
    #     <p>Hello world</p>
    #     <p>Goodbye world</p>
    #   </Typography>
    # </Paper>

    with mui.Paper:
        with mui.Typography:
            html.p("Hello world")
            html.p("Goodbye world")
with elements("properties"):

    # <Paper> 요소에 속성을 추가하는 예시
    #
    # "주어진 요소에 대한 모든 가능한 매개변수를 찾으려면,
    # MUI 위젯의 경우 mui.com에서, Monaco 편집기의 경우
    # https://microsoft.github.io/monaco-editor/에서 등
    # 관련 문서를 참조할 수 있습니다."

    # <Paper elevation={3} variant="outlined" square>
    #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
    # </Paper>

    with mui.Paper(elevation=3, variant="outlined", square=True):
        mui.TextField(
            label="My text input",
            defaultValue="Type here",
            variant="outlined",
        )

    # "파이썬 키워드와 동일한 매개변수를 전달해야 하는 경우,
    # 문법 오류를 피하기 위해
    # 밑줄(_)을 추가할 수 있습니다."
    #
    # <Collapse in />

    mui.Collapse(in_=True)

    # mui.collapse(in=True)
    # > Syntax error: 'in' is a Python keyword:


with elements("style_mui_sx"):

    # "Material UI 요소에는 'sx' 속성을 사용하세요."
    #
    # <Box
    #   sx={{
    #     bgcolor: 'background.paper',
    #     boxShadow: 1,
    #     borderRadius: 2,
    #     p: 2,
    #     minWidth: 300,
    #   }}
    # >
    #   Some text in a styled box
    # </Box>

    mui.Box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 1,
            "borderRadius": 2,
            "p": 2,
            "minWidth": 300,
        },
    )


with elements("style_elements_css"):

    # "다른 모든 요소에는 'css' 속성을 사용하세요."
    #
    # <div
    #   css={{
    #     backgroundColor: 'hotpink',
    #     '&:hover': {
    #         color: 'lightgreen'
    #     }
    #   }}
    # >
    #   This has a hotpink background
    # </div>

    html.div(
        "This has a hotpink background",
        css={"backgroundColor": "hotpink", "&:hover": {"color": "lightgreen"}},
    )


import streamlit as st


with elements("callbacks_retrieve_data"):

    # 특정 이벤트에서 콜백을 실행할 수 있는 요소가 있습니다.
    #
    # const [name, setName] = React.useState("")
    # const handleChange = (event) => {
    #   // 여기에서 볼 수 있듯이 텍스트 필드 값은
    #   // event.target.value에 저장됩니다
    #   setName(event.target.value)
    # }
    #
    # <TextField
    #   label="여기에 텍스트를 입력하세요"
    #   onChange={handleChange}
    # />
    # 'my_text'라는 이름의 새 항목을 세션 상태에 초기화합니다.
    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    # 텍스트 필드가 변경될 때 이 함수가 호출됩니다.
    # 콜백에 전달되는 매개변수를 알기 위해서는,
    # 요소의 문서를 참조할 수 있습니다.
    def handle_change(event):
        st.session_state.my_text = event.target.value

    # 여기서 우리가 텍스트 필드에 입력한 것을 표시합니다.
    mui.Typography(st.session_state.my_text)

    # 그리고 여기서 'onChange' 속성에 우리의 'handle_change' 콜백을 제공합니다.
    mui.TextField(label="텍스트를 입력하세요", onChange=handle_change)

with elements("callbacks_sync"):

    # 위와 같이 콜백 매개변수를 Streamlit의 세션 상태에 저장하고 싶다면,
    # 특별한 함수인 sync()를 사용할 수도 있습니다.
    #
    # onChange 이벤트가 발생하면, 콜백은 이벤트 데이터 객체를 인수로 호출됩니다.
    # 아래 예시에서, 우리는 그 이벤트 데이터 객체를 세션 상태 항목 'my_event'와 동기화하고 있습니다.
    #
    # 이벤트가 여러 매개변수를 전달하는 경우, 필요한 만큼 많은 세션 상태 항목을 동기화할 수 있습니다:
    # >>> sync("my_first_param", "my_second_param")
    #
    # 이벤트의 첫 번째 매개변수를 무시하고 두 번째를 동기화하고 싶다면,
    # sync에 None을 전달하세요:
    # >>> sync(None, "second_parameter_to_keep")

    from streamlit_elements import sync

    if "my_event" not in st.session_state:
        st.session_state.my_event = None

    if st.session_state.my_event is not None:
        text = st.session_state.my_event.target.value
    else:
        text = ""

    mui.Typography(text)
    mui.TextField(label="Input some text here", onChange=sync("my_event"))


with elements("callbacks_lazy"):

    # 첫 두 예제와 같이, 텍스트 필드에 글자를 입력할 때마다 콜백이 호출되지만
    # 전체 앱도 함께 다시 로드됩니다.
    #
    # 모든 입력마다 전체 앱을 다시 로드하는 것을 피하기 위해서, 콜백을
    # lazy()로 감쌀 수 있습니다. 이것은 다른 비지연 콜백이 호출될 때까지
    # 콜백 호출을 지연시킵니다. 이 방법은 폼을 구현할 때 유용할 수 있습니다.
    from streamlit_elements import lazy

    if "first_name" not in st.session_state:
        st.session_state.first_name = None
        st.session_state.last_name = None

    if st.session_state.first_name is not None:
        first_name = st.session_state.first_name.target.value
    else:
        first_name = "John"

    if st.session_state.last_name is not None:
        last_name = st.session_state.last_name.target.value
    else:
        last_name = "Doe"

    def set_last_name(event):
        st.session_state.last_name = event

    # 이름과 성을 표시합니다
    mui.Typography("당신의 이름: ", first_name)
    mui.Typography("당신의 성: ", last_name)
    # first_name과 last_name 상태와 onChange를 지연시켜 동기화합니다.
    # 텍스트를 입력해도 값이 바로 동기화되지 않습니다.

    mui.TextField(label="당신의 이름", onChange=lazy(sync("first_name")))
    mui.TextField(label="성", onChange=lazy(sync("last_name")))
    # lazy()에 일반 파이썬 함수도 전달할 수 있습니다.
    name = st.session_state.first_name
    print(name)
    # 여기서 우리는 onClick에 비지연 콜백을 sync()를 사용해 제공합니다.
    # onClick 이벤트 데이터 객체를 가져오는 데 관심이 없으므로,
    # 아무 인자도 없이 sync()를 호출합니다.
    #
    # sync()나 일반 파이썬 함수를 사용할 수 있습니다.
    # 콜백이 lazy()로 감싸지 않는 한, 그 호출은
    # 모든 다른 지연된 콜백들의 트리거도 발동시킬 것입니다.
    mui.Button("Update first namd and last name", onClick=sync())


with elements("callbacks_hotkey"):

    # Invoke a callback when a specific hotkey sequence is pressed.
    #
    # For more information regarding sequences syntax and supported keys,
    # go to Mousetrap's project page linked below.
    #
    # /!\ Hotkeys work if you don't have focus on Streamlit Elements's frame /!\
    # /!\ As with other callbacks, this reruns the whole app /!\

    from streamlit_elements import event

    def hotkey_pressed():
        print("Hotkey pressed")

    event.Hotkey("g", hotkey_pressed)

    # If you want your hotkey to work even in text fields, set bind_inputs to True.
    event.Hotkey("h", hotkey_pressed, bindInputs=True)
    mui.TextField(label="Try pressing 'h' while typing some text here.")

    # If you want to override default hotkeys (ie. ctrl+f to search in page),
    # set overrideDefault to True.
    event.Hotkey("ctrl+f", hotkey_pressed, overrideDefault=True)

    # with elements("callbacks_interval"):

    #     # Invoke a callback every n seconds.
    #     #
    #     # /!\ As with other callbacks, this reruns the whole app /!\

    #     def call_every_second():
    #         print("Hello world")

    # event.Interval(1, call_every_second)


keyword = "비트코인"
from datetime import datetime

now = datetime.now()
formatteed_date = now.strftime("%y%m%d")

with elements("dashboard"):
    # Streamlit Elements에서 제공하는 모든 요소를 사용하여 드래그하고 크기를 조정할 수 있는 대시보드를 만들 수 있습니다.

    from streamlit_elements import dashboard

    # 먼저, 대시보드에 포함시키고 싶은 모든 요소에 대해 기본 레이아웃을 구성하세요.

    layout = [
        # 매개변수: element_identifier, x_pos, y_pos, width, height, [항목 속성...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # 다음으로, 'with' 문법을 사용하여 레이아웃을 가진 대시보드를 생성합니다. 첫 번째 매개변수로 레이아웃을 취하고, GitHub 링크에서 찾을 수 있는 추가 속성들을 사용할 수 있습니다.

    with dashboard.Grid(layout):
        with mui.Paper(key="first_item"):
            mui.CardMedia(
                image=f"../graph/{formatteed_date}/{keyword}_graph.png",
                style={"height": 0, "paddingTop": "56.25%"},
            )
    # 사용자가 대시보드 항목을 이동하거나 크기를 조정할 때 업데이트된 레이아웃 값을 검색하려면, onLayoutChange 이벤트 매개변수에 콜백을 전달할 수 있습니다.

    def handle_layout_change(updated_layout):
        # 레이아웃을 파일에 저장하거나, 원하는 대로 처리할 수 있습니다.
        # 저장된 레이아웃을 복원하고 싶다면 dashboard.Grid()에 다시 전달할 수 있습니다.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("첫 번째 항목", key="first_item")

        mui.Paper("두 번째 항목 (드래그할 수 없음)", key="second_item")
        mui.Paper("세 번째 항목 (크기 조정할 수 없음)", key="third_item")


with elements("nivo_charts"):
    # Streamlit Elements는 Nivo에 의해 구동되는 45개의 데이터 시각화 컴포넌트를 포함하고 있습니다.

    from streamlit_elements import nivo

    DATA = [
        {"맛": "과일같은", "샤르도네": 93, "카르메네르": 61, "시라": 114},
        {"맛": "쓴", "샤르도네": 91, "카르메네르": 37, "시라": 72},
        {"맛": "무거운", "샤르도네": 56, "카르메네르": 95, "시라": 99},
        {"맛": "강한", "샤르도네": 64, "카르메네르": 90, "시라": 30},
        {"맛": "햇볕이 잘 드는", "샤르도네": 119, "카르메네르": 94, "시라": 103},
    ]

    with mui.Box(sx={"height": 500}):
        nivo.Radar(
            data=DATA,
            keys=["샤르도네", "카르메네르", "시라"],
            indexBy="맛",
            valueFormat=">-.2f",
            margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
            borderColor={"from": "color"},
            gridLabelOffset=36,
            dotSize=10,
            dotColor={"theme": "background"},
            dotBorderWidth=2,
            motionConfig="wobbly",
            legends=[
                {
                    "anchor": "top-left",
                    "direction": "column",
                    "translateX": -50,
                    "translateY": -40,
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "itemTextColor": "#999",
                    "symbolSize": 12,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#000"}}],
                }
            ],
            theme={
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                },
            },
        )


with elements("media_player"):

    # Play video from many third-party sources: YouTube, Facebook, Twitch,
    # SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, DailyMotion and Kaltura.
    #
    # This element is powered by ReactPlayer (GitHub link below).

    from streamlit_elements import media

    media.Player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True)
