//
//  Shader.fsh
//  aaa
//
//  Created by 会田 誠 on 11/04/30.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

varying lowp vec4 colorVarying;

void main()
{
    gl_FragColor = colorVarying;
}
