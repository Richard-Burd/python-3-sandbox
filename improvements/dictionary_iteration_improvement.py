# Capt. Chris offers a refactored solution for the 'dictionary iteration' section
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
 'bio': "I was a plumber and a doctor"
 },
}

# there is no need loop over the keys and the values,
# we can just search for the values alone
def work_history_profession_finder(users, profession):
  for user_value in users.values():
    for work_value in user_value['work-history'].values():
      if work_value == profession:
        print(f'{user_value.get("name")} was a {profession}')
work_history_profession_finder(users, 'doctor')
