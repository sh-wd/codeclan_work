class NakatomiPlaza:
    def __init__(self, floor1, floor2, floor3):
        self.floor1 = floor1
        self.floor2 = floor2
        self.floor3 = floor3

    def add_to_floor(self, floor, bad_guy):
        if floor.floor_number == floor:
            floor.append(bad_guy)

    # def smoke_em_like_it_aint_no_thang(self, , )
    
