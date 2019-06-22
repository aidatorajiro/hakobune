//
//  Shader.vsh
//  aaa
//
//  Created by 会田 誠 on 11/04/30.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

attribute vec4 position;
attribute vec4 color;

varying vec4 colorVarying;

uniform float translate;

void main()
{
    gl_Position = position;
	gl_Position.y += sin(translate) / 2;

    colorVarying = color;
}
