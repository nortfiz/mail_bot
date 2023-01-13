product_name_1="a-500"
product_name_2="jung-a-550"
product_name_3="a-creation"
product_name_4="a-flow"
product_name_5="as-500"
product_name_6="cd-500"
product_name_7="eco-profi"
product_name_8="eco-profi-deco"
product_name_9="eco-profi-standart"
product_name_10="ls-990"
product_name_11="ls-design"
product_name_12="ls-plus"
product_name_13="sl-500"
files =[f'json/{product_name_1}/page_source_all_{product_name_1}.json',
         f'json/a-550/page_source_all_jang-a-550.json',
         f'json/{product_name_3}/page_source_all_{product_name_3}.json',
         f'json/{product_name_4}/page_source_all_{product_name_4}.json',
         f'json/{product_name_5}/page_source_all_{product_name_5}.json',
         f'json/{product_name_6}/page_source_all_{product_name_6}.json',
         f'json/{product_name_7}/page_source_all_{product_name_7}.json',
         f'json/{product_name_8}/page_source_all_{product_name_8}.json',
         f'json/{product_name_9}/page_source_all_{product_name_9}.json',
         f'json/{product_name_10}/page_source_all_{product_name_10}.json',
         f'json/{product_name_11}/page_source_all_{product_name_11}.json',
         f'json/{product_name_12}/page_source_all_{product_name_12}.json',
]
with open(f'json/page_source_all.json', "w") as outfile:
   outfile.write('{}'.format('\n'.join([open(f, "r").read() for f in files])))

