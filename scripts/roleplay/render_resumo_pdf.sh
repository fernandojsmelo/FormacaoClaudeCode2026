#!/bin/bash
# render_resumo_pdf.sh NN "fonte;line-height" (na pasta de trabalho, com resNN.fixed.txt e metaNN.json) -> renderiza ResumoRolePlayNN com o CSS dado
n=$1; python3 - "$2" "$n" <<'P'
import json,sys
m=json.load(open(f'meta{sys.argv[2]}.json')); m['body_css']='body{font-size:%s}\ntable{break-inside:avoid}'%sys.argv[1]; json.dump(m,open(f'meta{sys.argv[2]}.json','w'),ensure_ascii=False,indent=1)
P
python3 "$(dirname "$0")/render_resumo.py" res$n.fixed.txt meta$n.json ResumoRolePlay$n.html && echo -n "$2 -> " && "$(dirname "$0")/build_pdf.sh" ResumoRolePlay$n.html
