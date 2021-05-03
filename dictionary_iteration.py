users = {
  'user-1': {
    'name':"Sam",

    'work-history' : {
      'job-1' : 'server',
      'job-2' : 'dentist'
    },

    'bio': "I was a server and a dentist"
  },

  'user-2': {
    'name':"Dan",

    'work-history' : {
      'job-1' : 'plumber',
      'job-2' : 'doctor'
    },

    'bio': "I was a plumber then an doctor"
  },
}

def work_history_profession_finder(users, profession):
  for user_key, user_value in users.items():
    for category_key, category_value in user_value.items():
      if category_key == 'bio' and profession in category_value:
        print(f'{user_value.get("name")} was a {profession}')

def bio_profession_finder(users, profession):
  for user_key, user_value in users.items():
    for category_key, category_value in user_value.items():
      if category_key == 'work-history':
        for job_key, job_value in category_value.items():
          if profession in job_value:
            print(f'{user_value.get("name")} was a {profession}')

work_history_profession_finder(users, 'doctor')
bio_profession_finder(users, 'dentist')
