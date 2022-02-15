cd TLPUI
python3 setup.py --command-packages=stdeb.command bdist_deb
sudo dpkg -i deb_dist/python3-tlpui_*all.deb
cd ..
