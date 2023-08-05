from svgdiagram.elements.group import Group
from svgdiagram.elements.rect import Rect
from svgdiagram.elements.svg_element import INF_CON


class WrapRect(Group):
    def __init__(self, child, padding_px=10, radius_px=8) -> None:
        super().__init__()
        self.child = child
        self.padding_px = padding_px
        self.radius_px = radius_px

    def _layout(self,
                x_con_min=-INF_CON, x_con_max=INF_CON,
                y_con_min=-INF_CON, y_con_max=INF_CON):
        c_xmin, c_xmax, c_ymin, c_ymax = self.child.bounds

        self.append_child(Rect(
            c_xmin-self.padding_px,
            c_ymin-self.padding_px,
            c_xmax-c_xmin+2*self.padding_px,
            c_ymax-c_ymin+2*self.padding_px,
            rx=self.radius_px,
            ry=self.radius_px,
        ))

        self.append_child(self.child)

        return super()._layout(x_con_min, x_con_max, y_con_min, y_con_max)
