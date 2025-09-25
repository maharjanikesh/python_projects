def number_of_videos(video_size, video_unit, drive_size, drive_unit):

    units = {
        'B' : 1,
        'KB': 1000,
        'MB': 1000**2,
        'GB': 1000**3,
        'TB': 1000**4,
    }
    # Converting video unit and drive unit into bytes
    video_unit_in_num = units[video_unit] * video_size
    drive_unit_in_num = units[drive_unit] * drive_size

    # Checking if video unit and drive unit is in Bytes
    if video_unit not in ['B', 'KB', 'MB', 'GB']:
        return "Invalid video unit"
    if drive_unit not in ['GB', 'TB']:
        return "Invalid drive unit"

    
    # Calculating the number of videos which can fit in a drive
    if drive_unit_in_num > video_unit_in_num:
        units_fit = drive_unit_in_num//video_unit_in_num
        return units_fit
    else:
        return "Invalid drive unit"
    
    

    return video_size

print(number_of_videos(1.5, "GB", 2.2, "TB"))