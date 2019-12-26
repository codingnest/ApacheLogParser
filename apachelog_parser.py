import argparse, logging, re, smtplib, configparser, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def level_count(read_FH):
    '''
    Method will Extract all the valid IP Addresses and returns it's count
    return: Dictionary
    '''
    ip_count = {}
    for line in read_FH:
        match = re.search(
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
            line)
        if match:
            if match.group() in ip_count:
                ip_count[match.group()] += 1
            else:
                ip_count[match.group()] = 1
    return ip_count

def config_reader(filepath = None):
    '''
    Method parses config file, return dictionary of all the sections
    return: dictionary
    '''
    dict_option = {}
    config = configparser.ConfigParser()
    config.read(filepath)
    sections = config.sections()
    options = config.options(sections[0])
    for option in options:
        try:
            dict_option[option] = config.get(sections[0], option)
            if dict_option[option] == -1:
                logger.error("Please check Threshold Configuration File")
        except:
            dict_option[option] = None
    return dict_option

def send_mail(user, password, to_list, subject, body):
    '''
    Method sends mail to List of users using GMAIL credentials
    '''
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ",".join(to_list)
    msg['Subject'] = subject

    msg_body = MIMEText(body, 'html')
    msg.attach(msg_body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, ",".join(to_list), msg.as_string())
        server.quit()
        logger.info("Email Sent!!")
    except Exception as e:
        logger.error("Error: {}".format(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('Required Named arguments')
    requiredNamed.add_argument('-e', '--email', dest='email_id', required=True,
                               type=str, nargs='+')
    args = parser.parse_args()

    # Logger Configuration
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    fileHandler = logging.FileHandler(filename='app.log')  # Relative Path
    fileHandler.setFormatter(formatter)
    logger.setLevel(level=logging.DEBUG)  # Logging Level

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    # read Gmail UserName and Password from config File
    dict_config = config_reader('config.ini')  # Relative Path

    ip_count = {}
    try:
        with open('access_log.txt') as infile: #Relative Path
            ip_count = level_count(infile)
    except Exception as e:
        logger.error("File Exception {}".format(e))
        sys.exit(1)

    logger.debug("IP Count: {}".format(ip_count))
    msg_body = '''\
        <html>
            <head></head>
            <body>
                <p>Hey {},<br>
                <br>
                Following is the Log Message Count:<br>\
                '''.format(",".join(args.email_id))
    for key in ip_count:
        msg_body += "<b>"+key+" -> "+str(ip_count[key])+"<br></b>"

    msg_body += '''\
            </p>
            </body>
            </html>
            '''
    logger.debug("Message Body {}".format(msg_body))
    send_mail(dict_config['gmail_user'], dict_config['gmail_password'], args.email_id,
              'Apache Log Parser Results', msg_body)