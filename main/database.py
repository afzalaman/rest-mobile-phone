from typing import List
from models import MobilePhone, OsType


all_phones: List[MobilePhone] = [
    MobilePhone(Id=1, Name="X30", Brand="Nokia", Release=2022, OS=OsType.Android),
    MobilePhone(Id=2, Name="iPhone 14", Brand="Apple", Release=2022, OS=OsType.iOS),
    MobilePhone(Id=3, Name="Galaxy S22", Brand="Samsung", Release=2022, OS=OsType.Android),
    MobilePhone(Id=4, Name="Pixel 6", Brand="Google", Release=2021, OS=OsType.Android)
]