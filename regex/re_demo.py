# coding=utf-8

import re


def test_search():
    data = "abcdakdjd"
    pattern = r"a.*?d"  # 懒惰匹配：尽量匹配最短串
    # pattern = r"a.*d"  # 贪婪匹配：要匹配最长串
    match = re.search(pattern, data, re.S)
    r = match.group(0) if match else ""
    return r



def replace_subject_image_url(mat):
    if mat:
        return 'src="%s"' % ("http://115.159.122.45" + "/" + mat.group(1))

def render_subject_img(value):
    return re.sub(r'src=[\"\'](.*?)[\"\']', replace_subject_image_url, value)



if __name__ == "__main__":
    # print test_search()

    val = """<span class="desClass">中共中央办公厅于2017年3月印发了《关于推进“两学一做”学习教育常态化制度化的意见》，意见指出要把____作为查找和解决问题的重要途径，注意听取群众的意见和反馈，抓早抓小、防微杜渐。<img src="http://img.winlesson.com/images/f0444e74c1f8ca523d793e8161c25099.png" _src="http://img.winlesson.com/images/f0444e74c1f8ca523d793e8161c25099.png" style="user-select: none;"/></span>"""
    print render_subject_img(val)
