from rooms import rooms

rooms['outside'].n_to = None # will be "mine-entrance" after steel-grate is opened
rooms['mine-entrance'].s_to = rooms['outside']
rooms['mine-entrance'].n_to = rooms['overlook']
rooms['mine-entrance'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['mine-entrance']
rooms['narrow'].w_to = rooms['mine-entrance']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
