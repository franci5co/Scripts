find /home/francisco -name '*.pdf' -exec sh -c 'pdftotext "{}" - | grep --with-filename --label="{}" --color "PEREZ SAEZ SAMUEL ALEJANDRO"' \;

