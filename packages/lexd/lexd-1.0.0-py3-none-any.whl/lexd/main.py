import os
import contextlib

with contextlib.redirect_stdout(open(os.devnull, 'w')):
    import cv2
    import numpy as np
    import mediapipe as mp
    import mediapipe.python.solutions.face_mesh_connections as fm

class Landmarks:

  def __init__(self, *args, **kwargs):
    super(Landmarks, self).__init__()
    self.__author = "importFourmi"
    self.__args = args
    self.__kwargs = kwargs

    # 1 
    self.landmarks_detector()
    
    # 2
    self.parts_face = self.__set_parts_face__()

# 1 ______________________________________________________________________________________________________________________________________
  def landmarks_detector(self, max_num_faces=1, min_detection_confidence=0.9):
    """
    Fonction qui permet d'initialiser notre détecteur.

    :param (max_num_faces): nombre maximum de visages à détecter
    :param (min_detection_confidence): coeficient de certitude de détection

    :return: None
    """

    self.__landmarks_detector__ = mp.solutions.face_mesh.FaceMesh(max_num_faces=max_num_faces,
                                                              refine_landmarks=True,
                                                              min_detection_confidence=min_detection_confidence,
                                                              static_image_mode=True,
                                                              )
# 1 ______________________________________________________________________________________________________________________________________


# 2 ______________________________________________________________________________________________________________________________________
  def __frozenset_list__(self, pFrozenset):
    """
    Fonction qui transforme un frozenset en liste de points.

    :param frozenset: frozenset avec les points

    :return: la liste des points
    """

    return sorted(set(np.array(list(pFrozenset)).reshape(-1)))
  

  def __set_parts_face__(self):
    """
    Fonction qui renvoie pour chaque partie du visage les landmarks correspondants.

    :return: le dictionnaire des parties du visage
    """

    return {
        "LEFT_EYE": self.__frozenset_list__(fm.FACEMESH_LEFT_EYE),
        "LEFT_EYEBROW": self.__frozenset_list__(fm.FACEMESH_LEFT_EYEBROW),
        "LEFT_IRIS": self.__frozenset_list__(fm.FACEMESH_LEFT_IRIS),
        "LIPS": self.__frozenset_list__(fm.FACEMESH_LIPS),
        "RIGHT_EYE": self.__frozenset_list__(fm.FACEMESH_RIGHT_EYE),
        "RIGHT_EYEBROW": self.__frozenset_list__(fm.FACEMESH_RIGHT_EYEBROW),
        "RIGHT_IRIS": self.__frozenset_list__(fm.FACEMESH_RIGHT_IRIS),
    }
# 2 ______________________________________________________________________________________________________________________________________


  def extract_landmarks(self, img, normalized=True):
    """
    Fonction qui retourne les landmarks d'un visage détécté sous le format [x, y, z(profondeur de chaque repère)].

    :param img: image
    :param (normalized): x et y normalisés si True / x et y en pixels si False

    :return: une liste de dimensions (478, 3) si un visage est détécté
    """

    results = self.__landmarks_detector__.process(img)
    if results.multi_face_landmarks:
        rows, cols = img.shape[:2]

        list_landmarks = list(results.multi_face_landmarks[0].landmark)
        if normalized:
            return np.array([[i.x, i.y, i.z] for i in list_landmarks])

        else:
            return np.array([[i.x*cols, i.y*rows, i.z] for i in list_landmarks])
    else:
        return np.array([])


# 3 ______________________________________________________________________________________________________________________________________
  def parts_face_mean(self, landmarks):
    """
    Fonction qui retourne un dictionnaire avec les coordonnées du centre de chaque partie du visage.

    :param img: image

    :return: le dictionnaire si un visage est détécté
    """

    if np.any(landmarks):
        center_dic = {}
        for key, value in self.parts_face.items():
            center_dic[key] = np.array([landmarks[ld] for ld in value]).mean(axis=0)
        return center_dic

    else:
        return np.array([])


  def __parts_face_selected__(self, landmarks):
    """
    Fonction qui retourne un dictionnaire avec le centre des lèvres et des iris.

    :param img: image

    :return: le dictionnaire si un visage est détécté
    """

    dictionnaire = self.parts_face_mean(landmarks)
    if np.any(dictionnaire):
        select = ["LEFT_IRIS", "LIPS", "RIGHT_IRIS"]
        return {key: value for key, value in dictionnaire.items() if key in select}

    else:
        return np.array([])
        

  def part_box(self, landmarks):
    nex_dic = {}
    for part_name, idx in self.parts_face.items():
      L = [landmarks[i] for i in idx]
      nex_dic[part_name] = np.append(np.array(L).min(axis=0)[0:2], np.array(L).max(axis=0)[0:2])
    return nex_dic
    
    
  def align_face(self, img, landmarks, coef=0.3):
    """
    Fonction qui aligne un visage toujours dans la même position.

    Parameters
    ----------
        - img: image

    Returns
    -------
        - l'image alignée
    """

    rows, cols = img.shape[:2]

    pts1 = self.__parts_face_selected__(landmarks)

    D = {}
    D["LEFT_IRIS"] = [0.65, 0.42]
    D["LIPS"] = [0.50,  0.75]
    D["RIGHT_IRIS"] = [0.35, 0.42]

    pts = np.array([D["LEFT_IRIS"], D["LIPS"], D["RIGHT_IRIS"]])

    if np.any(pts1):

        pts1 = np.array([pts1["LEFT_IRIS"][:2], pts1["LIPS"][:2], pts1["RIGHT_IRIS"][:2]])
        pts2 = (pts+coef/2)/(1+coef)

        for i in range(3):
            pts1[i][0] *= cols
            pts1[i][1] *= rows

            pts2[i][0] *= cols
            pts2[i][1] *= rows


        M = cv2.getAffineTransform(np.float32(pts1), np.float32(pts2))
        return cv2.warpAffine(img.copy(), M, (cols, rows))

    else:
        return np.array([])
# 3 ______________________________________________________________________________________________________________________________________


class Lexd(Landmarks):

    def __init__(self, *args, **kwargs):
        super(Lexd, self).__init__()
        self.__author = "importFourmi"
        self.__args = args
        self.__kwargs = kwargs
        self.methods = [f for f in dir(self) if not f.startswith('_')]
        self.version = "1.0.0"


        if self.__kwargs.get("verbose") == 1:
            print("Welcome to Lexd, the available functions are as follows and you can use help(function) for more information:")
            for fonction in self.methods:
                print("  -", fonction)