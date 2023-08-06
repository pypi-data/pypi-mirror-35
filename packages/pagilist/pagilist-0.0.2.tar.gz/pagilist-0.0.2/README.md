# Pagilist

Simple module to paginate lists using page or limit/offset. Source code available at
[Github](https://github.com/jersobh/pagilist).

### Usage
<pre>
page = 0 #first page
limit = 3 #three items per page
page_sample = paginate(list, page, limit)

##OR##

offset = 3 #start from the fourth element on list
page_offset = paginate_offset(list, offset, 5) #get from the fourth element with a limit of 5 elements

print(page_sample) #outputs [1, 2, 3]
print(page_offset) #outputs [4, 5, 6, 7, 8]
</pre>