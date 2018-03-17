class Geometry:

    @classmethod
    def polygonPointIntersection(cls, point_list, point):
        """
        :param point_list: Reference to polygon object
        :param point: Reference to point object
        :return: true if point is inside polygon
        """
        n = len(point_list)
        inside = False
        x,y = point.x, point.y

        p1x, p1y = point_list[0]
        for i in range(n + 1):
            p2x, p2y = point_list[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    @classmethod
    def pointLineIntersects(cls, segment, point):
        p1x, p1y = segment[0]
        p2x, p2y = segment[1]
        valor = (p2.y - p1.y)*point.x + (p1.x - p2.x)*point.y - p1.x*(p2.y - p1.y) - p1.y*(p1.x - p2.x)
        return (p2.y - p1.y) * valor < 0 and ((p1.y <= point.y < p2.y) or (p2.y <= point.y < p1.y))

    @classmethod
    def insideBoundingBox(cls, point_list, point):

        xmax = -100000
        xmin =  100000
        ymax = -100000
        ymin =  100000
        for p in point_list:
            xmax = max(p.x, xmax)
            xmin = min(p.x, xmin)

            ymax = max(p.y, ymax)
            ymin = min(p.y, ymin)

        return xmin <= point.x < xmax and ymin <= point.y < ymax