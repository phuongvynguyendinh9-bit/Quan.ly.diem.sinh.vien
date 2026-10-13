import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

# 1. Tạo DataFrame
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà',
                  'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Điểm chuyên cần': [8.0, 9.0, 7.5, 8.5, 7.0,
                        6.0, 9.0, 7.0, 8.0, 9.5],
    'Điểm giữa kỳ': [7.0, 8.0, 6.5, 9.0, 7.5,
                     6.5, 8.5, 7.5, 7.0, 8.5],
    'Điểm cuối kỳ': [8.5, 7.5, 8.0, 8.5, 7.0,
                     6.0, 9.0, 8.0, 8.5, 9.0]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df['Tổng kết'] = (
    0.2 * df['Điểm chuyên cần']
    + 0.3 * df['Điểm giữa kỳ']
    + 0.5 * df['Điểm cuối kỳ']
)

# 3. Xếp loại sinh viên
def xeploai(dtk):
    if dtk >= 8.5:
        return 'Giỏi'
    elif dtk >= 7.0:
        return 'Khá'
    elif dtk >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xeploai)

# 4. Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.divider()

# 5. Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết của 10 sinh viên")

df_hienthi = df.copy()
df_hienthi['Tổng kết'] = df_hienthi['Tổng kết'].round(2)

st.dataframe(df_hienthi, use_container_width=True, hide_index=True)

# 6. Thống kê chung
st.subheader("2. Thống kê chung")

dtk_trung_binh = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5).sum()

cot1, cot2, cot3 = st.columns(3)

cot1.metric("Điểm trung bình lớp", f"{dtk_trung_binh:.2f}")
cot2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
cot3.metric("Tổng số sinh viên", len(df))

st.write(
    f"**Sinh viên có điểm cao nhất:** "
    f"{sv_max['Họ và tên']} ({sv_max['Tổng kết']:.2f})"
)

st.write(
    f"**Sinh viên có điểm thấp nhất:** "
    f"{sv_min['Họ và tên']} ({sv_min['Tổng kết']:.2f})"
)

# 7. Tra cứu thông tin sinh viên
st.subheader("3. Tra cứu thông tin sinh viên")

ten_sv = st.selectbox(
    "Chọn tên sinh viên:",
    df['Họ và tên']
)

thongtin = df[df['Họ và tên'] == ten_sv].iloc[0]

st.write(f"**Họ và tên:** {thongtin['Họ và tên']}")

c1, c2, c3 = st.columns(3)

c1.metric("Điểm chuyên cần", f"{thongtin['Điểm chuyên cần']:.1f}")
c2.metric("Điểm giữa kỳ", f"{thongtin['Điểm giữa kỳ']:.1f}")
c3.metric("Điểm cuối kỳ", f"{thongtin['Điểm cuối kỳ']:.1f}")

c4, c5 = st.columns(2)

c4.metric("Điểm tổng kết", f"{thongtin['Tổng kết']:.2f}")
c5.metric("Xếp loại", thongtin['Xếp loại'])

# 8. Biểu đồ cột điểm tổng kết
st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")

fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(
    df['Họ và tên'],
    df['Tổng kết'],
    color='skyblue'
)

ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên")
ax.set_xlim(0, 10)
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.invert_yaxis()

for i, value in enumerate(df['Tổng kết']):
    ax.text(value + 0.1, i, f"{value:.2f}", va='center')

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 9. Thông tin người tạo ứng dụng
st.divider()

st.markdown(
    """
    <p style="text-align: right; font-size: 12px; color: gray;">
        Họ tên: NGUYỄN ĐINH PHƯƠNG VY - MSSV: 001308059313
    </p>
    """,
    unsafe_allow_html=True
)
```
