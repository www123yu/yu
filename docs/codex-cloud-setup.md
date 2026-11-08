# Codex �ƶ˻�������

��˵������ Codex Cloud��GitHub Codespaces �Ŀ��������������� `cloud-setup.md`�����ߵĻ�����Ҫ�ֱ�ʵ�ʴ��������ա�

## ������ѡ��ֿ�

1. �ڡ������ƶ˻���������ȷ�� GitHub �˺�Ϊ `www123yu`��
2. ѡ�� `www123yu/yu` �ֿ�� `main` ��֧���������ʼ���á���Get started����
3. ���ֿ��б�û�и��£���ˢ�£������ GitHub Ӧ���Ƿ��øòֿ�ķ���Ȩ�ޡ�

## ��ֱ�ӽ��������������ֵ�˵��

```text
��Ϊ����������ӿ��вֿ����� Python 3.12 �ƶ˻�����

��װ requirements-dev.txt����Ҫ Notebook ʱ�ٰ�װ requirements-notebooks.txt��
Ĭ�ϰ�װ NumPy��SciPy��Matplotlib��Pandas��SymPy��python-control �� Ruff��

��װ��ɺ�ʵ��ִ�в����棺
python -m pip check
python -m ruff check .
python examples/check_environment.py

����������ֵ������������ơ������Ƶ�����ͼ�����ݴ�����
MATLAB/Simulink��PLECS��LTspice ��ǰֻ����Դģ�ͣ���Ҫ���У���ȷ��������װ��
����ϵͳ������֤���������� Buck �Ĵ�����������ɿ��ط��档

������ Web ���񣬲������ⲿ�˿ڣ��������˺ſ��������֤��
���¼ʵ�ʰ�װ�� Python �������汾����ָ���κ���δ��ɵļ�顣
```

��������Ҫ��װ������� Python 3.12 ��׼���ã���ʹ�ã�

```bash
python -m pip install -r requirements-dev.txt
python -m pip check
python -m ruff check .
python examples/check_environment.py
```

��װ����ʱӦ������������ Python ���������ļ�����վ�㣻���������ڼ��������Χ��ʵ���о��������á�

## ����

�鿴�������ñ��棬ȷ��������ʵ��ͨ����û��ȱʧ���ʻ�δ��ɰ�װ���������ò��������������ַ��������ʾ���ٴӸû��������о�����

�ֿ���� `.devcontainer/devcontainer.json` Ϊ Codespaces ���廷�������ܵ�ƾ���ļ����϶� Codex Cloud �����á�GitHub Actions Ҳ��Ҫ�ڲֿ���ʵ�����к����ա�

�ο� [OpenAI �ٷ��ƶ˻���˵��](https://learn.chatgpt.com/docs/environments/cloud-environments)��
