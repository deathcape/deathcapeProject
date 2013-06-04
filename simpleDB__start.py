import boto


AWS_ACCESS_KEY = sys.argv[1] 
AWS_ACCESS_SECRET = sys.argv[2]

sdb = boto.connect_sdb(AWS_ACCESS_KEY, AWS_ACCESS_SECRET)
# domain = sdb.create_domain('deathcapeDomain')
domain = sdb.get_domain('deathcapeDomain')

item = domain.new_item('item1')
item['key1'] = 'value1'
item['key2'] = 'value2'

item.save()

for item in domain:
	print item.name
