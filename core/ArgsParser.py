import click
from .IPP import ImagePreProcesor
from .CCI import CloudCoverageIndex as cci



def createIPP(**kwargs):
    path = '{0}'.format(kwargs['image'])
    i = ImagePreProcesor(path)
    wr = path.split('/')
    name = wr[-1].split('.')
    image_name = name[0]

    if kwargs['n']:
        i.process(night_shift=True)
    else:
        i.process()
    
    if kwargs['s']:
        i.display(image='b&w')
    if kwargs['w']:
        i.write(image_name)
    if kwargs['d']:
        i.display()

    clouds = cci(i.fetchImageType(type='b&w'))
    print('\tCCI for image {} is {} ({}%)'.format(wr[-1], clouds.CCI(), clouds.CCI(as_percentaje=True)))


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings= CONTEXT_SETTINGS)
@click.version_option('2.12.06')
@click.option(
    '-s', 
    is_flag=True,
    help="Display processed image used to calculate CCI"
)
@click.option(
    '--w', 
    is_flag=True, 
    help="Save a copy of the processed image"
)
@click.option(
    '--d', 
    is_flag=True, 
    help="Display original image"
)
@click.option(
    '--n', 
    is_flag=True, 
    help="Process a night-time image"
)
@click.argument('image')
def initialize(**kwargs):
    createIPP(**kwargs)