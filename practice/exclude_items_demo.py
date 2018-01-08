# coding=utf-8

# [法一］continue
boxes = cached_all_boxes_by_platform_id(params.get('platform_id', 0))

result = []
for box in boxes:
    if BoxType.to_s(box.box_type) == 'poll' and cmp_ver(params['ver'], '5.9') < 0:
        continue
    elif BoxType.to_s(box.box_type) == 'interaction_image' and cmp_ver(params['ver'], '5.10.3') < 0:
        continue
    elif BoxType.to_s(box.box_type) == 'interaction_star' and cmp_ver(params['ver'], '5.10.3') < 0:
        continue
    elif BoxType.to_s(box.box_type) == 'interaction_history' and cmp_ver(params['ver'], '5.10.3') < 0:
        continue
    elif BoxType.to_s(box.box_type) == 'interaction_album' and cmp_ver(params['ver'], '5.10.3') < 0:
        continue
    else:
        res = self.details_of_box(box=box, params=params)
        result.append(res)

# [法二] 列表
boxes = cached_all_boxes(platform='iphone')

exclude_type_list = []
if cmp_ver(params['ver'], '4.1') < 0:
    exclude_type_list.append(BoxType.to_i('game'))
if cmp_ver(params['ver'], '5.0') < 0:
    exclude_type_list.extend([BoxType.to_i(box_type) for box_type in ['h5', 'video_list', 'banner']])
if cmp_ver(params['ver'], '5.1') < 0:
    exclude_type_list.append(BoxType.to_i('recommend'))
if cmp_ver(params['ver'], '5.3') < 0:
    exclude_type_list.append(BoxType.to_i('navigation'))
if cmp_ver(params['ver'], '5.4.1') < 0:
    exclude_type_list.append(BoxType.to_i('text'))
if cmp_ver(params['ver'], '5.8') < 0:
    exclude_type_list.append(BoxType.to_i('laifeng'))
if cmp_ver(params['ver'], '5.11') < 0:
    exclude_type_list += (BoxType.to_i('advertisement'),)

boxes = [box for box in boxes if box.box_type not in exclude_type_list]

