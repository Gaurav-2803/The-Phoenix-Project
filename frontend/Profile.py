import streamlit as st

# from ..backend.auth import (
#     get_github_oauth_session,
#     github_login_url,
#     fetch_github_token,
# )

from auth import get_github_oauth_session, github_login_url, fetch_github_token


# GitHub OAuth session setup
github_session = get_github_oauth_session()
login_url = github_login_url(github_session)[0]

if "key" not in st.session_state:
    st.set_page_config(
        page_title="Profile",
    )
    st.title("Self Healing System")
    st.link_button("Login with GitHub", login_url, type="primary")

    # print(f"url : {st.experimental_get_query_params()}")
    # if "code" not in st.session_state:
    #     st.session_state.code = st.experimental_get_query_params().get("code", [None])[
    #         0
    #     ]
    # token = fetch_github_token(github_session, st.session_state.code)
    # st.session_state.key = "value"
else:
    st.write("Already Logged In")
