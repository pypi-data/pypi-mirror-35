"""A Wrapper for the mail command line"""

import subprocess as sbp


def sendmail(subject="objet", body=b"bit sting body"):
    """Sand the emal to Antoine Tavant"""
    adress = "antoine.tavant@lpp.polytechnique.fr"
    iout = sbp.run(["mail", "-s", subject, adress], input=body)
    print(iout)


if __name__ == "__main__":
    sendmail("test", b"o\n")
