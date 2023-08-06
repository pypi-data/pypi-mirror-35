#!/usr/bin/env python3
import logging
import numpy as np
import os.path
import pandas as pd
import ruamel.yaml as ry
import textwrap

logger = logging.getLogger(__name__)


class Bow(object):
    """The pybow representation of a bow.

    Stores bow metadata and iterates over its limbs.

    Attributes:
        name: An identifying name for the bow.
        source: The source of the artefact’s data, or the bow’s designer.
        material: The material the bow is made of.
        date: A chronological dating of the bow.
        description: A textual description of the bow.

        find_date: Date of when the artefact has been found.
        provenience: The artefact’s find spot.
        preservation: The artefact’s state of preservation.
        arch_context: The artefact’s stratigraphical context.

        tags: A set of custom strings with categorical information about
            the bow.

    Properties:
        abslength: The bow’s complete length.
        ntnlength: The bow’s nock-to-nock length. NaN if the bow has no 2
            complete limbs.

    Methods:
        add_limb(): Add a limb to the bow.
        del_limb(): Delete a limb from the bow.
        write(): Write the bow object to disk.
    """
    def __init__(self, name, source,
                 material=None,
                 date=None,
                 # archaeological attributes unimplemented for the time being
                 # find_date=None,
                 # provenience=None,
                 # preservation=None,
                 # arch_context=None,
                 description=None,
                 tags=(),
                 limbs=()):
        """Construct a new bow object.

        Args: (when deviating from class docstring)
            limbs: A list of dataframes or a list of lists with input for
                Bow.add_limb(). Will add limbs to Bow object on init.

        Returns:
            A bow object.
        """
        self.name = name
        self.source = source
        self.material = material
        self.date = date
        # archaeological attributes unimplemented for the time being
        # self.find_date = find_date
        # self.preservation = preservation
        # self.provenience = provenience
        # self.arch_context = arch_context
        self.description = description
        self.tags = set(tags)
        self._limbs = ()
        for limb in limbs:
            # TODO: find a neater solution for this
            if isinstance(limb, pd.DataFrame):
                self.add_limb(limb)
            else:
                self.add_limb(*limb)

    def __getitem__(self, ix):
        if ix >= len(self):
            raise IndexError('Limb index out of range: {ix}'.format(ix=ix))
        else:
            return self._limbs[ix]

    def __len__(self):
        """Return the number of limbs in the bow."""
        return len(self._limbs)

    def __repr__(self):
        args = ['name', 'source']

        rep_obj = 'pb.Bow'
        rep_args = [repr(self.__dict__[arg])
                    for arg in args]
        rep_kwargs = [key + '=' + repr(val)
                      for key, val in self.__dict__.items()
                      if key not in args and not key.startswith('_')]
        rep_limbs = 'limbs=[' + ', '.join([repr(l) for l in self._limbs]) + ']'

        return rep_obj + '(' + ', '.join(rep_args+rep_kwargs+[rep_limbs]) + ')'

    def __str__(self):
        width = 32
        manual_line_keys = {'name', 'source', 'tags', 'description'}
        table_keys = [k
                      for k in self.__dict__.keys()
                      if not (k.startswith('_')
                              or k in manual_line_keys)]

        title_lines = [self.name, '(' + self.source + ')']
        table_lines = [k + ': ' + str(self.__dict__[k])
                       for k in sorted(table_keys)]
        tag_line = 'tags: ' + ', '.join(self.tags)
        desc_line = 'description: ' + self.description
        separator = '-' * width
        lines = [*title_lines,
                 separator,
                 *table_lines,
                 tag_line,
                 desc_line]
        return '\n'.join([textwrap.fill(l, width=width, subsequent_indent='  ')
                          for l in lines])

    @property
    def abslength(self):
        return sum(limb.abslength for limb in self)

    @property
    def ntnlength(self):
        if False not in [limb.complete for limb in self]:
            return sum(limb.length for limb in self)
        else:
            return np.nan

    def add_limb(self, df, complete=True, tags=()):
        """Add a limb to the bow.

        Args:
            df (pandas.DataFrame): A dataframe containing measurements for a
                limb. Must contain columns 'l', 'width', and 'thickness' at
                minimum.
            complete (bool): Whether or not the measurements describe a
                complete, unbroken limb. (default: True)
            tags (iterable): A list of custom strings with categorical
                the limb.

        Returns:
            -

        Raises:
            TypeError when trying to exceed the maximum number of limbs per
                bow. (2)
        """
        new_limb = Limb(self, df, complete, tags)
        new_limb_tuple = self._limbs + (new_limb,)
        if len(new_limb_tuple) <= 2:
            self._limbs = new_limb_tuple
        else:
            raise TypeError('Trying to add more than 2 limbs to a bow.')

    def del_limb(self, ix):
        """Delete a limb from the bow.

        Args:
            ix: The numerical index of the limb to be deleted.

        Returns:
            -

        Raises:
            IndexError for an ix that indicates a limb not in the bow.
        """
        try:
            del_limb = self[ix]
            new_limb_tuple = tuple(limb for limb in self if limb != del_limb)
            self._limbs = new_limb_tuple
        except IndexError:
            raise

    def _make_yamldict(self, basename):
        bow_args = ['name', 'material', 'date', 'source', 'description',
                    # 'find_date', 'provenience', 'preservation',
                    # 'arch_context',
                    'tags']
        yaml_dict = {arg: getattr(self, arg)
                     for arg in bow_args
                     if getattr(self, arg)}

        limb_list = []
        for ix, limb in enumerate(self):
            limb_fname = basename + '_' + str(ix) + os.path.extsep + 'csv'
            limb_yamldict = {'data': limb_fname}
            if not limb.complete:
                limb_yamldict['complete'] = limb.complete
            if limb.tags:
                limb_yamldict['tags'] = list(limb.tags)
            limb_list.append(limb_yamldict)
        if limb_list:
            yaml_dict['limbs'] = limb_list
        return yaml_dict

    def write(self, fname):
        """Write the bow to disk.

        Bow objects get written to up to three files:
        * a basename.yaml file with bow/limb metadata and a manifest.
        * one or two basename_n.csv for the limb measurement DataFrames.

        Args:
            fname: A filename or file basename.

        Returns:
            -
        """
        base_path = os.path.dirname(os.path.abspath(fname))
        base_fname = os.path.splitext(os.path.basename(fname))[0]

        yaml_dict = self._make_yamldict(base_fname)

        yamlfile = os.path.join(base_path, base_fname + os.extsep + 'yaml')
        with open(yamlfile, 'w') as f:
            yaml = ry.YAML()
            yaml.dump(yaml_dict, f)
            logger.debug('Written bow metadata to file %s', yamlfile)
            for ix, limb in enumerate(yaml_dict['limbs']):
                csvfile = os.path.join(base_path, limb['data'])
                self[ix].data.to_csv(csvfile, index=False)
                logger.debug('Written limb measurements to file %s', csvfile)


class Limb(object):
    """A pybow representation of a limb.

    Attributes:
        data: The pandasDataFrame containing this limb’s measurements.
        complete: Whether or not this limb is complete and unbroken.
        tags: A set of custom strings with categorical information about
            the limb

    Properties:
        name: A compound name of this limb’s index position and the bow’s name.
        material: The material this limb is made of. (The limb's bow’s
            material attribute.)
        abslength: This limb’s absolute length – including projections beyond
            the nock.
        length: This limb’s functional length – measuring no further than the
            nock.
    """
    def __init__(self, parent, df, complete, tags):
        try:
            self._validate_df(df)
            self._parent = parent
            self.data = df
            self.complete = complete
            self.tags = set(tags)
        except ValueError:
            raise

    def __repr__(self):
        rep_df = 'pd.DataFrame(' + \
            str(self.data.values.tolist()) + \
            ', columns=' + \
            str(list(self.data.columns)) + \
            ')'
        rep_complete = str(self.complete)
        rep_tags = repr(self.tags)
        return '[' + ', '.join([rep_df, rep_complete, rep_tags]) + ']'

    @property
    def name(self):
        return self._parent.name+'_'+str(self._parent._limbs.index(self))

    @property
    def material(self):
        return self._parent.material

    @property
    def abslength(self):
        return self.data['l'].max() - self.data['l'].min()

    @property
    def length(self):
        return self.data['l'].max()

    def _validate_df(self, df):
        required_columns = {'l', 'width', 'thickness'}
        required_types = (int, float)
        if not required_columns.issubset(df.columns):
            raise ValueError("Limb DataFrame does not contain required " +
                             "columns." +
                             "\nRequired: ['l', 'width', 'thickness']" +
                             "\nGiven: {cols}".format(cols=list(df.columns)))
        elif False in [df[c].dtype in required_types
                       for c in required_columns]:
            errors = [(col, df[col].dtype)
                      for col in required_columns
                      if df[col].dtype not in required_types]
            raise TypeError("Wrong data type in required column." +
                            "\nRequired: int or float" +
                            "\nGiven: {errors}".format(errors=errors))
        else:
            for col in [c for c in required_columns if df[c].dtype == int]:
                logger.warning("Column %s has data type int. " +
                               "float is recommended.",
                               col)
            pass


def read(fname):
    """Read a bow object from disk.

    Args:
        fname: The file name of a bow’s .yaml file.

    Returns:
        A pb.Bow() object.
    """
    basepath = os.path.dirname(os.path.abspath(fname))

    yaml = ry.YAML()
    with open(fname, 'r') as f:
        parsed_yaml = yaml.load(f)
        logger.debug('Read bow metadata from file %s', fname)

    args = []
    for arg in ['name', 'source']:
        try:
            args.append(parsed_yaml[arg])
        except KeyError:
            raise ValueError(fname +
                             "does not contain required attribute: " +
                             arg)

    kwargs = {}
    for kwarg in ['material', 'date', 'description', 'tags',
                  # 'find_date', 'provenience', 'preservation', 'arch_context'
                  ]:
        try:
            kwargs[kwarg] = parsed_yaml[kwarg]
        except KeyError:
            logger.debug('No metadata for %s in %s, passing.', kwarg, fname)
            pass

    limbs = []
    for ix, limb in enumerate(parsed_yaml['limbs']):
        csvfile = os.path.join(basepath, limb['data'])
        df = pd.read_csv(csvfile, index_col=None)
        logger.debug('Read limb measurements from %s', csvfile)
        try:
            complete = limb['complete']
        except KeyError:
            complete = True
            logger.debug("No completeness metadata for limb %s found " +
                         "in file %s. Assuming True.",
                         ix, fname)
        try:
            tags = limb['tags']
        except KeyError:
            tags = []
            logger.debug("No tag metadata for limb %s found " +
                         "in file %s. Assuming None.",
                         ix, fname)
        limbs.append([df, complete, tags])

    return Bow(*args,
               **kwargs,
               limbs=limbs)
