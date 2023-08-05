import numpy as np
from typing import Union


def numpy_hex_string_array_to_int(numpyarray: Union[list, np.ndarray]) -> np.ndarray:
    numpyarray = np.char.array(numpyarray)
    numpyarray = numpyarray.lower()
    alldtypes = {
        255: np.uint8,
        65535: np.uint16,
        4294967295: np.uint32,
        18446744073709551615: np.uint64,
    }
    try:
        is_with_0x = numpyarray[0][:2] == "0x"
        if is_with_0x:
            np.char.array(numpyarray)
            numpyarray = numpyarray.replace("0x", "")
    except Exception:
        pass
    startlength = 0

    togetmaxbytepossible = numpyarray.astype("U").dtype.itemsize // 4
    bytelength = togetmaxbytepossible
    rightdatatype_ = sum([16**x for x in range(togetmaxbytepossible)]) * 15
    rightdatatype = "uint64"
    for kkey in list(alldtypes):
        if kkey >= rightdatatype_:
            rightdatatype = alldtypes[kkey]
            break
    onebytearray = np.ascontiguousarray(
        numpyarray.view("S1")
        .reshape((-1, numpyarray.itemsize * 2))
        .T[::4]
        .T.reshape((-1, bytelength + startlength))[
            :, startlength : bytelength + startlength
        ]
    ).view("u1")
    filterarray = np.array(
        [
            48,
            49,
            50,
            51,
            52,
            53,
            54,
            55,
            56,
            57,
            97,
            98,
            99,
            100,
            101,
            102,
            65,
            66,
            67,
            68,
            69,
            70,
        ],
        dtype=np.uint8,
    )
    condlist = [
        onebytearray == filterarray[0],
        onebytearray == filterarray[1],
        onebytearray == filterarray[2],
        onebytearray == filterarray[3],
        onebytearray == filterarray[4],
        onebytearray == filterarray[5],
        onebytearray == filterarray[6],
        onebytearray == filterarray[7],
        onebytearray == filterarray[8],
        onebytearray == filterarray[9],
        onebytearray == filterarray[10] | filterarray[16],
        onebytearray == filterarray[11] | filterarray[17],
        onebytearray == filterarray[12] | filterarray[18],
        onebytearray == filterarray[13] | filterarray[19],
        onebytearray == filterarray[14] | filterarray[20],
        onebytearray == filterarray[15] | filterarray[21],
    ]
    choicelist = np.array(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        dtype=np.uint8,
    )
    stan_val = np.uint8(0)
    bytevaluesarray = np.select(condlist, choicelist, stan_val)

    bitshiftnp = np.array(
        list(reversed([x * 4 for x in range(bytelength)])), dtype=rightdatatype
    )
    rightposition = bytevaluesarray.T
    readytoconcat = []
    loop_ = rightposition.shape[0]
    for bitsh in range(loop_ - 1):
        readytoconcat.append(
            np.left_shift(
                rightposition[bitsh : bitsh + 1][0].astype(rightdatatype),
                bitshiftnp[bitsh],
            )
        )
    readytoconcat.append(bytevaluesarray.T[loop_ - 1 : loop_][0])
    rightposition = np.vstack(readytoconcat).T
    together = np.sum(rightposition, axis=1, dtype=rightdatatype)
    return together



