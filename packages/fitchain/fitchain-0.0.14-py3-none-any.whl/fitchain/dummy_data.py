import faker as fk
import pandas as pd

import random
# from random import randint
import string as s
from faker.providers import BaseProvider
from fitchain import constants

from fitchain.fitter import Fitter


class FitchainDataProvider(BaseProvider):
    """ Create new provider class (fitchain customized) """

    def integer_with_n_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return random.randint(range_start, range_end)

    def float_with_n_digits(self, n, gt=1, lt=10):
        return round(random.uniform(gt, lt), n)

    def string_with_n_chars(n):
        strlen = random.randint(n)
        dummy_str = (''.join(random.choice(s.ascii_letters + ' ') for i in range(strlen)))
        return dummy_str


class DummyData:
    """ Generate dummy data from dict(schema) """

    def __init__(self, schema):
        self.schema = schema
        # print('From DummyData', type(self.schema))

    def generate_data(self):
        # For more complex types check https://github.com/joke2k/faker
        fake = fk.Faker()
        fake.add_provider(FitchainDataProvider)
        # print('Generating %s fake records from schema'%numrecords)
        if self.schema['format'] == 'pandas.dataframe':
            data = {}

            fitter = Fitter()

            # scan each field and generate dummy
            for field in self.schema['fields']:
                # print('\nProcessing field', field['name'])
                dummy_content = []
                types = field['type'].keys()
                # print('types=', types)
                stats = field['stats']
                lens = stats['length']
                # print('stats=', stats)
                # Prioritize distribution estimation (if any)
                if 'distrib' in field:
                    print('Generating data for column %s' % field['name'])
                    # by construction there is only one type with distrib
                    nelems = list(field['type'].values())[0]
                    print('field=', field['distrib'])
                    dist_name, dist_params = field['distrib']['name'], field['distrib']['params']
                    pdf, sample = fitter.make_pdf(dist_name, dist_params, size=nelems)
                    dummy_content = list(sample)

                else:
                    for t in types:
                        nelems = field['type'][t]  # elements of this type
                        # print('Current type=', t, 'num_elements=', nelems, 'lens=', lens)
                        ###############################
                        # Fake primitive types
                        ###############################
                        if t == constants.FITCHAIN_INT:
                            for l in lens:
                                n = int(l)
                                r = lens[l]
                                # print(n,r, type(n), type(r), int(nelems*r))
                                numrecs = int(nelems * r)
                                # print('Generating numrecs=', numrecs, 'with n=', n, 'digits')
                                for i in range(numrecs):
                                    dummy_int = fake.integer_with_n_digits(n)
                                    dummy_content.append(dummy_int)

                        if t == constants.FITCHAIN_STRING:
                            for l in lens:
                                n = int(l)
                                r = lens[l]
                                # print(n,r, type(n), type(r), int(nelems*r))
                                numrecs = int(nelems * r)
                                # print('Generating numrecs=', numrecs, 'with n=', n, 'digits')
                                for i in range(numrecs):
                                    dummy_str = fake.pystr(n, n)
                                    dummy_content.append(dummy_str)

                        if t == constants.FITCHAIN_FLOAT:
                            for l in lens:
                                n = int(l)
                                r = lens[l]
                                numrecs = int(nelems * r)
                                # print('Generating numrecs=', numrecs, 'with n=',n, 'digits')
                                for i in range(numrecs):
                                    dummy_float = fake.float_with_n_digits(n)
                                    # dummy_float = fake.pyfloat(1,2)
                                    dummy_content.append(dummy_float)

                        if t == constants.FITCHAIN_BOOL:
                            for i in range(nelems):
                                dummy_bool = fake.pybool()
                                dummy_content.append(dummy_bool)

                        ###############################
                        # Fake complex types
                        ###############################
                        if t == constants.FITCHAIN_EMAIL:
                            for i in range(nelems):
                                dummy_content.append(fake.email())

                        if t == constants.FITCHAIN_ADDRESS:
                            for i in range(nelems):
                                dummy_address = fake.address()
                                dummy_content.append(dummy_address)

                        if t == constants.FITCHAIN_NAME:
                            for i in range(nelems):
                                dummy_name = fake.name()
                                dummy_content.append(dummy_name)

                        if t == constants.FITCHAIN_DATETIME:
                            for i in range(nelems):
                                dummy_time = fake.time()
                                dummy_content.append(dummy_time)

                # Fill dataframe by column
                data[field['name']] = dummy_content

                """    
                for t in types:
                    nelems = field['type'][t]  # elements of this type
                    #print('Current type=', t, 'num_elements=', nelems, 'lens=', lens)

                    ###############################
                    # Fake primitive types
                    ###############################                    
                    if t == constants.FITCHAIN_INT:
                        for l in lens:
                            n = int(l)         
                            r = lens[l]
                            #print(n,r, type(n), type(r), int(nelems*r))
                            numrecs = int(nelems*r)
                            #print('Generating numrecs=', numrecs, 'with n=', n, 'digits')
                            for i in range(numrecs):
                                dummy_int = fake.integer_with_n_digits(n)
                                dummy_content.append(dummy_int)

                    if t == constants.FITCHAIN_STRING:
                        for l in lens:
                            n = int(l)         
                            r = lens[l]
                            #print(n,r, type(n), type(r), int(nelems*r))
                            numrecs = int(nelems*r)
                            #print('Generating numrecs=', numrecs, 'with n=', n, 'digits')
                            for i in range(numrecs):
                                dummy_str = fake.pystr(n,n) 
                                dummy_content.append(dummy_str)

                    if t == constants.FITCHAIN_FLOAT:
                        for l in lens:
                            n = int(l)         
                            r = lens[l]
                            numrecs = int(nelems*r)
                            #print('Generating numrecs=', numrecs, 'with n=',n, 'digits')
                            for i in range(numrecs):
                                dummy_float = fake.float_with_n_digits(n)
                                #dummy_float = fake.pyfloat(1,2)
                                dummy_content.append(dummy_float)

                    if t == constants.FITCHAIN_BOOL:
                        for i in range(nelems):
                            dummy_bool = fake.pybool()
                            dummy_content.append(dummy_bool)

                    ###############################
                    # Fake complex types
                    ###############################
                    if t == constants.FITCHAIN_EMAIL:
                        for i in range(nelems):
                            dummy_content.append(fake.email())

                    if t == constants.FITCHAIN_ADDRESS:
                        for i in range(nelems):
                            dummy_address = fake.address()
                            dummy_content.append(dummy_address)

                    if t == constants.FITCHAIN_NAME:
                        for i in range(nelems):
                            dummy_name = fake.name()
                            dummy_content.append(dummy_name)

                    if t == constants.FITCHAIN_DATETIME:
                        for i in range(nelems):
                            dummy_time = fake.time()
                            dummy_content.append(dummy_time)

                # Fill dataframe by column
                data[field['name']] = dummy_content
                """

            # Convert to dataframe and return
            # df = pd.DataFrame(data=data)
            df = pd.DataFrame.from_dict(data, orient='index')
            df = df.transpose()
            df.reset_index(drop=True)
            print('Generated data', df.shape)
            return df
