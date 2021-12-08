import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d


def draw_horizon(redshift, distance, universeType, imageNumber):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw a circle on the x=0 'wall'
    p = Circle((4500, 4500), distance)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=redshift, zdir="x")

    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 9000)
    ax.set_zlim(0, 9000)
    ax.set_xlabel('Redshift')
    ax.set_ylabel('Distance (Mpc)')
    ax.set_zlabel('Distance (Mpc)')
    ax.set_title(
        'Horizon Radius ≈ ' + str(int(distance)) + ' Mpc at Redshift ≈ ' + str(int(redshift))
    )

    plt.savefig('images_' + str(universeType) + '/image' + str(int(imageNumber)) + '.png')
    plt.close(fig)
    # plt.show()

