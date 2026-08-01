import pyradox as pyx
from pathlib import Path
import random

def process_file():
	"""处理目录下的所有txt文件"""
	input_dir = Path.cwd()
	output_dir = input_dir / "processed"
	
	# 创建输出目录
	output_dir.mkdir(exist_ok=True)

	subideo = []
	ideo_totol = 100
	# 递归遍历所有txt文件
	for file_path in input_dir.rglob("*.txt"):
		try:
			with file_path.open('r', encoding='utf-8') as f:
				content = f.read()
				pyxContent = pyx.parse(content)
				party_politics = pyxContent["set_politics"]
				match party_politics["ruling_party"]:
					case "communism":
						party_politics["ruling_party"] = "totalism"
					case "progressism":
						party_politics["ruling_party"] = "progressivism"
					case "democratic":
						party_politics["ruling_party"] = "liberalism"
					case "neutrality":
						party_politics["ruling_party"] = "authoritarianism"
					case "dictatorship":
						party_politics["ruling_party"] = "paternalism"
					case "fascism":
						party_politics["ruling_party"] = "suprematism"
					case "destruction_system":
						party_politics["ruling_party"] = "mysticism"
					
				ideology_group = pyxContent["set_popularities"]
				print(file_path)
				ideology_group_i = [i for i, v in ideology_group.items()]
				ideology_group_v = [v for i, v in ideology_group.items()]
				print("before: ")
				print(ideology_group_i)
				print(ideology_group_v)
				j = len(ideology_group_i)
				for i in range(j):
					if "reconcilism" in ideology_group_i[i]:
						del ideology_group_i[i]
						del ideology_group_v[i]
						break
				j = len(ideology_group_i)
				totol = 0
				for i in range(j):
					if "communism" in ideology_group_i[i]:
						ideology_group_i[i] = "totalism"
					elif "progressism" in ideology_group_i[i]:
						ideology_group_i[i] = "progressivism"
					elif "democratic" in ideology_group_i[i]:
						ideology_group_i[i] = "liberalism"
					elif "neutrality" in ideology_group_i[i]:
						ideology_group_i[i] = "authoritarianism"
					elif "dictatorship" in ideology_group_i[i]:
						ideology_group_i[i] = "paternalism"
					elif "fascism" in ideology_group_i[i]:
						ideology_group_i[i] = "suprematism"
					elif "destruction_system" in ideology_group_i[i]:
						ideology_group_i[i] = "mysticism"
					totol = totol+int(ideology_group_v[i])
				if totol < 100:
					ideo_totol = 100 - totol
					v1 = random.randint(0,len(ideology_group_v)-1)
					ideology_group_v[v1] = ideology_group_v[v1] + ideo_totol
				elif totol > 100:
					ideo_totol = totol - 100
					while ideology_group_v[v2] < ideo_totol:
						v2 = random.randint(0,len(ideology_group_v)-1)
					ideology_group_v[v2] = ideology_group_v[v2] - ideo_totol
				if "socialism" in ideology_group:
					del ideology_group["socialism"]
				if "communism" in ideology_group:
					del ideology_group["communism"]
				if "neutrality" in ideology_group:
					del ideology_group["neutrality"]
				if "dictatorship" in ideology_group:
					del ideology_group["dictatorship"]
				if "democratic" in ideology_group:
					del ideology_group["democratic"]
				if "conservatism" in ideology_group:
					del ideology_group["conservatism"]
				if "progressism" in ideology_group:
					del ideology_group["progressism"]
				if "reconcilism" in ideology_group:
					del ideology_group["reconcilism"]
				if "fascism" in ideology_group:
					del ideology_group["fascism"]
				if "destruction_system" in ideology_group:
					del ideology_group["destruction_system"]
				dicte = ["totalism","socialism","progressivism","liberalism","conservatism","authoritarianism","paternalism","suprematism","mysticism"]
				ideology_group_i1, ideology_group_v1 = reorder_parallel_lists(ideology_group_i, ideology_group_v, dicte)
				j = len(ideology_group_i1)
				for i in range(j):
					ideology_group[ideology_group_i1[i]] = ideology_group_v1[i]
				ideology_group_i2 = [i for i, v in ideology_group.items()]
				ideology_group_v2 = [v for i, v in ideology_group.items()]
				print("after: ")
				print(ideology_group_i2)
				print(ideology_group_v2)

				print("\n")
			newcontent = str(pyxContent)
			newcontent2 = newcontent.replace("    ", "\t")
			# 构建输出路径
			rel_path = file_path.relative_to(input_dir)
			output_path = output_dir / rel_path
			
			# 保持目录结构
			output_path.parent.mkdir(parents=True, exist_ok=True)
			
			# 写入新文件
			with output_path.open('w+', encoding='utf-8') as f:
				f.write(newcontent2)
				
					
		except Exception as e:
			print(f"处理 {file_path.name} 时出错: {str(e)}")

def reorder_parallel_lists(a, b, new_order):
	order_map = {element: idx for idx, element in enumerate(new_order)}
	combined = list(zip(a, b))
	sorted_combined = sorted(combined, key=lambda pair: order_map[pair[0]])
	sorted_a, sorted_b = zip(*sorted_combined)

	return list(sorted_a), list(sorted_b)

if __name__ == "__main__":
	print("开始处理文件...")
	process_file()
	print("处理完成！结果保存在:", Path.cwd() / "processed")