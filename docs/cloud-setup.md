# GitHub �ƶ�����ָ��

## 1. �˺���ֿ�

����Ŀʹ�� [`www123yu/yu`](https://github.com/www123yu/yu)������֧Ϊ `main`���� Codex ��ѡ��ֿ�ʱ��ȷ�������� GitHub �˺�Ϊ `www123yu`��

���޷����زֿ⣬�Ⱥ˶������ӵ��û������ټ��� GitHub Ӧ���Ƿ��ñ��ֿ����Ȩ�ޡ���ҳ��¼״̬���ѱ����Ӧ����Ȩ�˺���Ҫ�ֱ�ȷ�ϡ�

## 2. ���ػ�ȡ���ύ

��¡���вֿⲢ����Ŀ¼��

```bash
git clone https://github.com/www123yu/yu.git
cd yu
```

��ȷ�� Git �������Լ����ύ���������䡣�� README ��װ Python ����������޸ĺ�ִ�м�飬���ύ�����ͣ�

```bash
python -m pip check
python -m ruff check .
python examples/check_environment.py
git add .
git status --short
git commit -m "Describe the research change"
git push
```

�״����Ͱ� Git �ĵ�¼��ʾ��� GitHub ��Ȩ���ύǰ��� `git status --short`��ȷ��û���˺�ƾ�ݡ�����֤��δ����Ȩ�����ݻ��������ҵģ�͡�

## 3. �ƶ˿������Զ��������

1. �ڲֿ�� `Code �� Codespaces` �´��� `main` ���ƶ˻�����`.devcontainer/devcontainer.json` �ᶨ�� Python ��������װ���裻�μ� [��������˵��](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)��
2. ��װ���������ƶ��ն�ִ�� README ������������ȷ���˳����Ϊ 0�������ļ��޸ĺ��ؽ�����ʹ�޸���Ч��
3. �� `Actions`��ȷ���״��ύ�����ļ��ͨ������ҳ��Ҫ������ Actions����ҳ����ʾ���ú󣬴Ӹù��������� `Run workflow`��
4. �ύһ��ʵ��ģ�ͻ�����ű��������ж�Ӧ�Ŀ�����֤����ǰ������鲻�������κ���ҵ��������
5. ���˻�ҳ��˶� Codespaces �� Actions ��������Ԥ�㣬����ʹ�ý�����ֹͣ������Ҫ�� Codespace������������ [Codespaces ���ٿ�ʼ](https://docs.github.com/en/codespaces/quickstart)��

���ؾ�̬���ͨ���������һ����ʵ�� Codespaces ������ Actions ���С�ֻ�����߾����պ󣬲ſɼ�Ϊ���ƶ�������ɡ���

## 4. ģ�͡����ļ�������

`.slx` �ȶ�����ģ�Ͱ������ƹ����������ı��ϲ���Сģ�Ϳ���������⣻Ƶ���޸ĵĶ�����ģ�ͺʹ��ļ��ɰ���Ŀʵ��������� Git LFS��LFS ���Զ���װ����Ԥ������ƷѰ��ţ�GitHub ����ͨ�ļ��� LFS �ļ��в�ͬ�����ƣ�����ǰ���� [Git LFS ˵��](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)��

����ȷ������ LFS ������������� `.slx` ģ�ͣ��Ȱ�װ Git LFS����ִ�У�

```bash
git lfs install
git lfs track "*.slx"
git add .gitattributes
```

�ⲻ��Ǩ�ƾ���ʷ����ģ���ѽ��ֿ�����ҪǨ�ƣ�Ӧ���й滮Ǩ�ƺ�Э����ͬ����

��������Դ�ļ�����ʼ���Ͳ����ű�������Ϳ��������ɵĲ���ͨ�����ύ��ԭʼʵ�������봦�������ݷֿ���������λ������/�����汾������Ƶ�ʡ��������������衢��Դ��У��ֵ����Ҫ���������ݼ���ʹ����ʽ���ݴ洢���񣬲��ڲֿ��¼ DOI ���ȶ����ӡ�

��ʽ�о����к󣬿ɱ������� Python ���嵥��

```bash
python -m pip freeze > results/python-environment.txt
```

����һ������ϵͳ��Python �汾�� Git �ύ ID�����嵥���ʵ�ʲ���ϵͳ������ŵ��ƽ̨�����ƻ���һ�¡�

## 5. ��ҵ�������ĺ�������

MATLAB / Simulink��PLECS��LTspice �ڱ�ģ�����ṩ�ļ������ṹ������û����Ϊ������ GitHub �ֿ���Զ�����ƶ˰�װ������֤��ִ��������

��Ҫ MATLAB / Simulink �Զ���ʱ���ɽ�һ��ѡ�� [MathWorks �� GitHub Actions ����](https://www.mathworks.com/help/matlab/matlab_external/use-matlab-with-github-actions.html)���ٰ����ò�Ʒ���ֿ�ɼ��ԡ�֧�ַ�Χ������֤���á�PLECS / LTspice ����������ð汾ȷ�ϰ�װ���������ӿڣ�Ҳ����ѡ���Ѱ�װ����ʹ��Ȩ�޵����й���������

�������ӷ��湤����ʱ����ȷ��¼ִ�������汾�����ɷ�ʽ��ģ�����롢������á�Ԥ��ָ�����ݲ��Ҫ��ȱ�ٷ�����������֤������£��Ѵ�������ʾ���������������������֤��
