import requests
from bs4 import BeautifulSoup


def spaceflightnow():
    url = 'https://spaceflightnow.com/launch-schedule/'
    request = requests.get(url)
    data_list = []
    status_code = request.status_code
    if (status_code != 200):
        return data_list
    else:
        page_content = requests.get(url).content

        css_tags = ['datename', 'missiondata' ,'missdescrip']

        soup = BeautifulSoup(page_content, 'html.parser')
        schedule_box = soup.find('div', attrs={'class': 'entry-content clearfix'})

        datename_data = schedule_box.find_all('div', attrs={'class': 'datename'})
        missiondata_data = schedule_box.find_all('div', attrs={'class': 'missiondata'})
        missdescrip_data = schedule_box.find_all('div', attrs={'class': 'missdescrip'})

        for index, value in enumerate(datename_data):
            launch_date = datename_data[index].find('span', attrs={'class': 'launchdate'}).text.strip()
            mission_str = datename_data[index].find('span', attrs={'class': 'mission'}).text.strip()
            mission_str_parts = mission_str.split('•')
            rocket = mission_str_parts[0].strip()
            mission = mission_str_parts[1].strip()
            launch_time_site_contents = missiondata_data[index].contents
            launch_time = launch_time_site_contents[1].strip()
            launch_site = launch_time_site_contents[3].strip()
            
            data_list.append({
                'launch_date': launch_date,
                'mission': mission,
                'rocket': rocket,
                'mission': mission,
                'launch_time': launch_time,
                'launch_site': launch_site
                })
        
        return data_list
