####################
#
# Copyright (c) 2018 Fox-IT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
####################

import logging
import traceback
import codecs

class OutputWorker(object):
    @staticmethod
    def write_worker(result_q, admin_filename, session_filename):
        """
            Worker to write the results from the results_q to the given files.
        """
        admin_out = codecs.open(admin_filename, 'w', 'utf-8')
        session_out = codecs.open(session_filename, 'w', 'utf-8')

        admin_out.write('ComputerName,AccountName,AccountType\n')
        session_out.write('UserName,ComputerName,Weight\n')
        while True:
            obj = result_q.get()

            if obj is None:
                logging.debug('Write worker obtained a None value, exiting')
                break

            t = obj[0]
            data = obj[1]
            if t == 'session':
                session_out.write(data)
            elif t == 'admin':
                admin_out.write(data)
            else:
                logging.warning("Type is %s this should not happen", t)

            result_q.task_done()

        logging.debug('Write worker is done, closing files')
        admin_out.close()
        session_out.close()
        result_q.task_done()
