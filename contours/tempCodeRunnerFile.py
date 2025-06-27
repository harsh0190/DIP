    contours,_ = cv.findContours(th_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print("\n\nCHAIN_APPROX_SIMPLE \n",contours)
