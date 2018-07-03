from imports import *
def Combine_Data():
	if (0):
		raw_data = gl.glob("O:/QUALITY/QC Data Project/Raw Data/*")
		print(raw_data)
		excel_file = ExcelWriter('CombinedData.xlsx')
		all_data = pd.DataFrame()
		for i in raw_data:
			df = pd.read_excel(i)
			all_data = all_data.append(df, ignore_index=True)
			print(all_data)
			all_data.to_excel(excel_file)
		excel_file.save()
	if (1):
		raw_data = gl.glob("O:/QUALITY/QC Data Project/Raw Data/*")
		print(raw_data)
		all_data = pd.DataFrame()
		for i in raw_data:
			df = pd.read_excel(i)
			all_data = all_data.append(df, ignore_index=True)
			print(all_data)
			all_data.to_csv('CombinedData.csv')

Combine_Data()
