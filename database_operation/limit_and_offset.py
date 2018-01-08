# coding=utf-8


@classmethod
def get_my_course_by_category(cls, userid, category, pageSize, pageNum):
    start = (pageNum - 1) * pageSize
    end = start + pageSize

    limit = pageSize
    offset = (pageNum - 1) * pageSize

    course_ids = []

    if category == "0":  # 免费课程
        sql = """
            SELECT tb1.courseId FROM course_user_info as tb1 
            inner join course_info as tb2 on tb2.courseId = tb1.courseId
            WHERE tb1.userId = '%s' and tb2.coursePrice = 0
            ORDER BY tb1.purchaseTime DESC 
            LIMIT %s OFFSET %s;
        """ % (userid, limit, offset)

        datas = SqlExcecute.fetch_all(sql)

        for data in datas:
            course_ids.append(data[0])

    elif category == "1":  # 付费课程
        sql = """
            SELECT tb1.courseId FROM course_user_info as tb1 
            inner join course_info as tb2 on tb2.courseId = tb1.courseId
            WHERE tb1.userId = '%s' and tb2.coursePrice > 0
            ORDER BY tb1.purchaseTime DESC 
            LIMIT %s OFFSET %s;
        """ % (userid, limit, offset)

        datas = SqlExcecute.fetch_all(sql)

        for data in datas:
            course_ids.append(data[0])

    else:
        user_courses = cls.objects.filter(user_id=userid).order_by("-purchase_time")[start:end]

        for user_course in user_courses:
            course_ids.append(user_course.course_id)

    all_course_info_dict = {}

    if course_ids:
        courses = CourseInfo.objects.filter(course_id__in=course_ids).order_by("-create_time")
        for course in courses:
            all_course_info_dict[course.course_id] = course.to_json()

    result_list = []

    for course_id in course_ids:
        course_dict = all_course_info_dict.get(course_id, {})
        if course_dict:
            result_list.append(course_dict)

    return result_list
