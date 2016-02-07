from subprocess import call, check_call
##import pyautogui
import os
import sys

if sys.platform == 'win32':
    def ScheduleEnding():
        next = open(os.environ["APPDATA"] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\next.bat','wb')
        next.write("start" + os.getcwd() + file_name)
        next.close()


    def unScheduleEnding():
        os.remove(os.environ["APPDATA"] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\next.bat')

else:
    def prompt_sudo():
        ret = 0
        if os.getenv("SUDO_USER") is None:
            msg = "[sudo] password for %u: "
            ret = check_call("sudo -v -p '%s'" % msg, shell=True)
        return ret


    def writeBashFile(excludes):
        temp = open("temp.sh", "wb")
        temp.write("#!/bin/bash\n")
        if excludes.get('flux') is None:
            temp.write('sudo add-apt-repository ppa:kilian/f.lux\n')
        if excludes.get('grub-customizer') is None:
            temp.write('sudo add-apt-repository -y ppa:danielrichter2007/grub-customizer\n')
        if excludes.get('chrome') is None:
            temp.write('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - \n')
            temp.write('sudo sh -c \'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list\'\n')
        if excludes.get('bitcoinxt') is None:
            temp.write('cat <<EOF | apt-key add -\n')
            temp.write('-----BEGIN PGP PUBLIC KEY BLOCK-----\n')
            temp.write('Comment: GPGTools - https://gpgtools.org\n')
            temp.write('\n')
            temp.write('mQINBFXPTUoBEADLYhZu9ZrtkAZog8dis59Cx+6CqAZhQBmMQPvUZ9+9NKxa7Jt4\n')
            temp.write('idZT1q+2FYmbl8hhUjtkAMW0zSrTrkTBUBjsi3mak6Ormdh1L6rApaSPY+jlizON\n')
            temp.write('IkoDyNf3BPEv4ccPhQi3AGXNyytgVhSIBu8kJAkrLCHMjMwA14WgM+Z7GljLCRIc\n')
            temp.write('IyBIpSG0gZYs5Uq3BoZzRytspRPTsIp/+wvyX+YsxlXXOg/vzcjwiCqVVEfMVfLq\n')
            temp.write('Ro8KXmnS1w2a9lBdK7M1RpftqJ3RUhbsywkyUakNdN17iUKbvGjc2OzmH+v5W/rw\n')
            temp.write('DT9o0ayJ7Oa9ufsSUKq10Ylt4obVK167gXZ8yQ/nICjev7Fqc/L97D0L4fetj1K2\n')
            temp.write('BNqD02iodhunK3BTDREGrUjmUL5CR5lyBlSu8GgIMeU7XyoCoJPgNa50zDCh8U+U\n')
            temp.write('SK0yfNx2kGv/6UwXe9VhFDouCLhk7ca3r8ELnnUEBPxHYtV3nGBcGrfm+1Hy5wlM\n')
            temp.write('Sx18LqjaP7No71TU9ZoYoKEyeoDv8ckTSfsrr5WAcDHID4vYhxIdt5tVKqxLKhn3\n')
            temp.write('sOTM5rwNJ32anwZnX19HNJX7GFEe7vw7hGiyiKnckCUSh0w5WVr1wptPzS1gaMcZ\n')
            temp.write('pl6IRL8ibxJ1co9lAKG3+nqF+Lkwwgvh9P75ZnPRMWQja9xnXaUJ7xWtFQARAQAB\n')
            temp.write('tDlCaXRjb2luIFhUIFNpZ25pbmcgQXV0aG9yaXR5IDxzaWduaW5nQGJpdGNvaW54\n')
            temp.write('dC5zb2Z0d2FyZT6JAjcEEwEKACEFAlXPTUoCGwMFCwkIBwMFFQoJCAsFFgIDAQAC\n')
            temp.write('HgECF4AACgkQOZxuTpe2lWvMwhAAt+JvmZOZCL0QH9Lhk+M08Nl6TyxIf53B/dK9\n')
            temp.write('mFdsUKnwoWlrJ1r46tCps10Air3IeKhNUvIPXvbuV1cQ5mVleQKOSj2Hg0TvaePU\n')
            temp.write('z/sLdyjUXRCOTEY/hr96YMR7SmTRa38b+4FYY/Oz5vDaOVZrOmf7x+sGd8IUdUxX\n')
            temp.write('YoFot/gliL1MR6/gaoGrL7iXsw8ZnWEWGLEx5KMOF7VLffPAsmMr7dqTpXx12xXa\n')
            temp.write('wqYn6S8raOFqAteOoDdZwSjiHQEivKM90KiZb5KsyEe9iso3I2PYWUcEgnuJL5rt\n')
            temp.write('z020KtGGyBwfT4NhWBC8RR5GRypTGyOkpnrpVDzArAKCL3u4t89SAh3TnC3E8mza\n')
            temp.write('3RXyFcucuw20/Dxj66imUtqcORVQr5QAtColQghZKKwK2WeJ3MlmK1UnjIipGNji\n')
            temp.write('imOmktl3e2P+2nHwPmRp8T3edYsIY0UnEtBtuShYQF2NGJ/Z18QzaBJ1nfdblnr9\n')
            temp.write('O+2vVJENRITpDR5rfTgVEHfRR6WL39xcJuMvITZP9dvGy1MRRrFAIrR+VtAv5QEe\n')
            temp.write('Z92trWqkeURZ4MnGNUnCow8rFR7dktOfOIykLSeqjCwMs8sR/qoRBaVIWXArinAj\n')
            temp.write('TdTaPwul1eVlRmq/tRI5j6xbEkidkq38vWgSlOh2PjH1FVy0zGnDwdlSHN1sNk9g\n')
            temp.write('cnMXk0U=\n')
            temp.write('=zxQ5\n')
            temp.write('-----END PGP PUBLIC KEY BLOCK-----\n')
            temp.write('EOF\n')
            temp.write('echo \'deb [ arch=amd64 ] http://bitcoinxt.software.s3-website-us-west-2.amazonaws.com/apt wheezy main\' > /etc/apt/sources.list.d/bitcoinxt.list\n')
        if excludes.get('spotify') is None:
        	temp.write('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886\n')
        	temp.write('sudo echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list\n')
        if excludes.get('ksuperkey') is None:
            temp.write('sudo add-apt-repository -y ppa:mehanik/ksuperkey\n')
        if excludes.get('steam') is None:
            temp.write('sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B05498B7\n')
            temp.write('sudo sh -c \'echo "deb http://repo.steampowered.com/steam/ precise steam" >> /etc/apt/sources.list.d/steam.list\'\n')
        temp.write('sudo apt-get update\n')
        if None in [excludes.get(x) for x in ['grub-customizer', 'dev-tools', 'chrome', 'bitcoinxt', 'ksuperkey', 'steam']]:
	    	temp.write('sudo apt-get install -y')
	    if excludes.get('grub-customizer') is None:
			temp.write(' grub-customizer')
	    if excludes.get('chrome') is None:
			temp.write(' google-chrome-stable')
	    if excludes.get('bitcoinxt') is None:
			temp.write(' bitcoinxt')
	    if excludes.get('steam') is None:
			temp.write(' steam')
	    if excludes.get('dev-tools') is None:
			temp.write(' python python-pip python3 python3-pip idle git')
	    if excludes.get('flux') is None:
            temp.write(' fluxgui')
        if excludes.get('spotify') is None:
        	temp.write(' spotify-client')
	    if excludes.get('ksuperkey') is None:
			temp.write(' ksuperkey\n')
			temp.write('ksuperkey')
	    	temp.write('\n')
        if excludes.get('upgrade') is None:
            temp.write('sudo apt-get upgrade -y\n')
        if excludes.get('autoremove') is None:
            temp.write('sudo apt-get autoremove -y\n')
        temp.flush()
        temp.close()
        
        
    def killBashFile():
        os.remove("temp.sh")


def executeWindows():
    import win32com.shell.shell as shell
    file_name = "InstallationAutomation.py"

    if sys.argv[-1] != 'asadmin':
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        sys.exit(0)

    if not os.path.exists(os.environ["APPDATA"] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\next.bat'):
        ScheduleEnding()
    else:
        unScheduleEnding()


def executeLinux():
    print("This program will install repositories and software on your machine without security policy overrides. If you do not consent to this, exit now.")
    import time
    for i in range(10):
        sys.stdout.write('\r')
        sys.stdout.write(str(10-i) + ' ' * (len(str(10-i+1)) - len(str(10-i))))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    if prompt_sudo():
        print("Try again when you have root access")
    else:
        print("Sudo access granted")
        writeBashFile({})
        call(["sudo", "sh", "temp.sh"])
        killBashFile()

if __name__ == "__main__":
    if sys.platform == 'win32':
        executeWindows()
    else:
        executeLinux()
