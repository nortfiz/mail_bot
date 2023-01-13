# product_name="ls-plus"
# files = [f'json/{product_name}/page_source_1_jung-{product_name}.json',
#          f'json/{product_name}/page_source_2_jung-{product_name}.json',
#          f'json/{product_name}/page_source_3_jung-{product_name}.json',
#          f'json/{product_name}/page_source_4_jung-{product_name}.json',
#          f'json/{product_name}/page_source_5_jung-{product_name}.json',
#          f'json/{product_name}/page_source_6_jung-{product_name}.json',
#          f'json/{product_name}/page_source_7_jung-{product_name}.json',
#          f'json/{product_name}/page_source_9_jung-{product_name}.json',
#          f'json/{product_name}/page_source_10_jung-{product_name}.json',
#          f'json/{product_name}/page_source_11_jung-{product_name}.json',
#          f'json/{product_name}/page_source_12_jung-{product_name}.json',
#          f'json/{product_name}/page_source_13_jung-{product_name}.json',
#          f'json/{product_name}/page_source_14_jung-{product_name}.json',
#          f'json/{product_name}/page_source_15_jung-{product_name}.json',
#          f'json/{product_name}/page_source_16_jung-{product_name}.json',
#          f'json/{product_name}/page_source_17_jung-{product_name}.json',
#          f'json/{product_name}/page_source_18_jung-{product_name}.json',
#          f'json/{product_name}/page_source_19_jung-{product_name}.json',
#          f'json/{product_name}/page_source_20_jung-{product_name}.json',
#          f'json/{product_name}/page_source_21_jung-{product_name}.json',
#          f'json/{product_name}/page_source_22_jung-{product_name}.json',
#          f'json/{product_name}/page_source_23_jung-{product_name}.json',
#          f'json/{product_name}/page_source_24_jung-{product_name}.json',
#          f'json/{product_name}/page_source_25_jung-{product_name}.json',
#          f'json/{product_name}/page_source_26_jung-{product_name}.json',
#          f'json/{product_name}/page_source_27_jung-{product_name}.json',
#          f'json/{product_name}/page_source_28_jung-{product_name}.json',
#          f'json/{product_name}/page_source_29_jung-{product_name}.json',
#          f'json/{product_name}/page_source_30_jung-{product_name}.json',
#          f'json/{product_name}/page_source_31_jung-{product_name}.json',
#          f'json/{product_name}/page_source_32_jung-{product_name}.json',
#          f'json/{product_name}/page_source_33_jung-{product_name}.json',
#          f'json/{product_name}/page_source_34_jung-{product_name}.json',
#          f'json/{product_name}/page_source_35_jung-{product_name}.json',
#          f'json/{product_name}/page_source_36_jung-{product_name}.json',
#          f'json/{product_name}/page_source_37_jung-{product_name}.json',
#          f'json/{product_name}/page_source_38_jung-{product_name}.json',
#          ]
# with open(f'json/{product_name}/page_source_all_{product_name}.json', "w") as outfile:
#    outfile.write('{}'.format('\n'.join([open(f, "r").read() for f in files])))



product_name_1="a-500"
product_name_2="a-550"
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
files = [f'json/{product_name_1}/page_source_all_{product_name_1}.json',
         f'json/{product_name_2}/page_source_all_{product_name_2}.json',
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