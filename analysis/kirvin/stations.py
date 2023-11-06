from zmq import IntEnum


class Station(IntEnum):
    IJMOND = 209
    VALKENBURG_ZH = 210
    VOORSCHOTEN = 215
    IJMUIDEN = 225
    DE_KOOY = 235
    SCHIPHOL = 240
    VLIELAND = 242
    WIJDENES = 248
    BERKHOUT = 249
    HOORN_TERSCHELLING = 251
    WIJK_AAN_ZEE = 257
    HOUTRIBDIJK = 258
    DE_BILT = 260
    SOESTERBERG = 265
    STAVOREN = 267
    LELYSTAD = 269
    LEEUWARDEN = 270
    MARKNESSE = 273
    DEELEN = 275
    LAUWERSOOG = 277
    HEINO = 278
    HOOGEVEEN = 279
    EELDE = 280
    HUPSEL = 283
    HUIBERTGAT = 285
    NIEUW_BEERTA = 286
    TWENTHE = 290
    CADZAND = 308
    VLISSINGEN = 310
    HOOFDPLAAT = 311
    OOSTERSCHELDE = 312
    VLAKTE_VAN_DE_RAAN = 313
    HANSWEERT = 315
    SCHAAR = 316
    WESTDORPE = 319
    WILHELMINADORP = 323
    STAVENISSE = 324
    HOEK_VAN_HOLLAND = 330
    THOLEN = 331
    WOENSDRECHT = 340
    ROTTERDAM_GEULHAVEN = 343
    ROTTERDAM = 344
    CABAUW_MAST = 348
    GILZE_RIJEN = 350
    HERWIJNEN = 356
    EINDHOVEN = 370
    VOLKEL = 375
    ELL = 377
    MAASTRICHT = 380
    ARCEN = 391

    @classmethod
    def create_int_string_mapping(cls) -> dict[str, str]:
        return {
            # create mapping from string number to station name
            # example: { "391": "arcen" }
            str(station.value): station.name.lower().replace("_", " ")
            for station in cls
        }
