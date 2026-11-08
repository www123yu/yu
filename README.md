# yu �� �������ӿ��й�����

����任��������������ƻ�·��ʵ�����ݷ����Ŀ��вֿ���㡣Python 3.12 ����������ֵ���㡢���Ʒ����������Ƶ������ݴ�����ģ��Դ�ļ������������ֱ������

GitHub �ֿ⣺[`www123yu/yu`](https://github.com/www123yu/yu)��

## ��ʼʹ��

�ֿ��ϴ� GitHub �󣬴� `Code �� Codespaces �� Create codespace on main`�����������ᰲװ���������ͼ�鹤�ߡ��ն˿��ú����У�

```bash
python -m pip check
python -m ruff check .
python examples/check_environment.py
```

����������֤��װ������ Buck �Ĵ�����ϵ�����������ؼ����桢�����ȶ�����֤��ʵ�������ƶ˻��������״�ʵ�ʴ�����֤��

���� Notebook�����ն˰�װ��ѡ������

```bash
python -m pip install -r requirements-notebooks.txt
```

����ʹ��ʱ���Ȱ�װ Python 3.12���������������⻷�����ٰ�װ `requirements-dev.txt`���������Windows PowerShell Ϊ `.\.venv\Scripts\Activate.ps1`��Linux/macOS Ϊ `source .venv/bin/activate`��

```bash
python -m venv .venv
# �������⻷����ִ����������
python -m pip install -r requirements-dev.txt
```

## �ļ���������

| ·�� | ���� |
| --- | --- |
| `models/simulink/` | MATLAB / Simulink / Simscape ģ����ű� |
| `models/plecs/` | PLECS ģ�͡���ʼ���Ͳ����ű� |
| `models/ltspice/` | LTspice ԭ��ͼ����������������ģ�� |
| `examples/` | С�Ϳ�����ʾ���뻷����� |
| `data/` | ԭʼ�����������ݣ���Ŀ¼˵�� |
| `results/` | ���Ρ�ͼ����ָ������в����Ŀ¼˵�� |
| `docs/` | ���á��������о�˵�� |

�ύģ��ʱͬʱ��¼�����汾�����������䡢���ˡ������뵥λ�����ƺͲ������ڡ���������á����в��輰�оݡ��ο����Ӧע����Դ���������Ӧ�ύ��

## �Զ����

`.github/workflows/checks.yml` �ṩ����һ���ԡ�Python ��̬���ͻ���ʾ����顣���ͨ��ֻ˵����Щ��Ŀͨ������ҵ��������Ӳ��ʵ�����赥�����С���¼�ͺ��顣

��������Ĭ��δ��װ MATLAB��Simulink��PLECS �� LTspice����Ҫ�Զ�������Щ���������һ��ȷ�ϲ���ϵͳ֧�֡���װ��ʽ������֤�Լ��ʺϵ��йܻ����й���������

## �����븴��

�״��ϴ���Codespaces ���ա�Git LFS ����ҵ������˵���� [GitHub �ƶ�����ָ��](docs/cloud-setup.md)���� Codex ��ʹ�òֿ�� [Codex �ƶ˻�������](docs/codex-cloud-setup.md)����Ŀ¼�����ļ��̶�ֱ�������汾��������ʽ�о�ʱ��������ʵ�����л��������������嵥������¼ģ�͡����ݺʹ���汾��

��ģ��δ��ѡ�о��ɹ��Ŀ�������֤������Դ���롢���ĸ��������ݼ�ǰ�������߰�ʵ��Ȩ��ѡ������֤��ע����������Դ��
